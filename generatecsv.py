import json
import csv
from data.data import prerequisites

# Load converted.json
with open('data/converted.json', 'r', encoding='utf-8') as f:
    converted = json.load(f)

# Build mapping from prerequisite text to list of (subject, course_code)
prereq_text_to_courses = {}
for subject, course_code, prereq_text in prerequisites:
    prereq_text_to_courses.setdefault(prereq_text, []).append((subject, course_code))

points = {}
links = []

def extract_points_and_links(prereq_obj, source_id, source_group, link_strength):
    if not prereq_obj:
        return

    if isinstance(prereq_obj, dict):
        node_type = prereq_obj.get('type')
        if node_type == 'ContentScoreRequirement':
            content = prereq_obj.get('content', {})
            content_type = content.get('type')
            if content_type == 'ContentCollegeCourse':
                cid = content['subject'] + " " + content['courseCode']
                points[cid] = content['subject']
                links.append((source_id, cid, link_strength))
            elif content_type == 'ContentExam':
                cid = content['exam']
                points[cid] = "Exam"
                links.append((source_id, cid, link_strength))
            elif content_type == 'ContentOtherCourse':
                cid = content['course']
                points[cid] = "HS Course"
                links.append((source_id, cid, link_strength))
        elif node_type == 'CollegeCourse':
            cid = prereq_obj['subject'] + " " + prereq_obj['course_code']
            points[cid] = prereq_obj['subject']
            links.append((source_id, cid, link_strength))
        elif node_type == 'ContentExam':
            cid = prereq_obj['exam']
            points[cid] = "Exam"
            links.append((source_id, cid, link_strength))
        elif node_type == 'ContentOtherCourse':
            cid = prereq_obj['course']
            points[cid] = "HS Course"
            links.append((source_id, cid, link_strength))
        elif node_type == 'PrerequisiteGroup':
            for child in prereq_obj.get('children', []):
                if prereq_obj.get('logic') == "AND":
                    extract_points_and_links(child, source_id, source_group, link_strength)
                else:
                    extract_points_and_links(child, source_id, source_group, link_strength / 2)
        # Ignore OtherRequirement, etc.

# Process each prereq_text and all associated courses
for prereq_text, prereq_data_list in converted.items():
    course_infos = prereq_text_to_courses.get(prereq_text)
    if not course_infos:
        continue  # skip if no course info

    # Handle both list and dict for prereq_data_list
    if isinstance(prereq_data_list, list):
        true_prereq = prereq_data_list[0]
    else:
        true_prereq = prereq_data_list

    prereq_obj = true_prereq['prerequisites']

    for subject, course_code in course_infos:
        source_id = subject + " " + course_code
        points[source_id] = subject  # Add the course itself as a point
        extract_points_and_links(prereq_obj, source_id, subject, 1)

# Remove points that do not have any links (as source or target)
linked_ids = set()
for source, target, _ in links:
    linked_ids.add(source)
    linked_ids.add(target)

points = {cid: group for cid, group in points.items() if cid in linked_ids}

# Calculate size: number of outgoing links for each point
from collections import Counter
size_counter = Counter()
for target, source, _ in links:
    if size_counter[source] < 5:
        size_counter[source] += 1

# Write points.csv
with open('data/points.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Group', 'url', 'size'])
    for cid, group in points.items():
        # Try to split cid into subject and course_code
        if group not in ("Exam", "HS Course"):
            try:
                subject, course_code = cid.split(" ", 1)
                url = f"https://planner.langaracs.ca/courses/{subject}/{course_code}"
            except ValueError:
                url = ""
        else:
            url = ""
        size = size_counter.get(cid, 0)
        writer.writerow([cid, group, url, size])


# Write links.csv
with open('data/links.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Source', 'Target', 'Value'])
    for source, target, value in links:
        writer.writerow([target, source, value])

# unique_groups = sorted(set(points.values()))
# for g in unique_groups:
#     print(g)

num_college_courses = sum(1 for cid, group in points.items() if group not in ("Exam", "HS Course"))
print(f"Number of college courses: {num_college_courses}")