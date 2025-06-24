import json
import csv
from data.data import prerequisites



# Load converted.json
with open('data/converted.json', 'r', encoding='utf-8') as f:
    converted = json.load(f)

# Build mapping from prerequisite text to (subject, course_code)
prereq_text_to_course = {}

for subject, course_code, prereq_text in prerequisites:
    prereq_text_to_course[prereq_text] = (subject, course_code)

points = {}
links = []

def extract_points_and_links(prereq_obj, source_id, source_group, link_strength):
    # assert prereq_obj
    if not prereq_obj:
        return
    
    if isinstance(prereq_obj, dict):
        node_type = prereq_obj.get('type')
        # Handle ContentScoreRequirement wrapper
        if node_type == 'ContentScoreRequirement':
            content = prereq_obj.get('content', {})
            content_type = content.get('type')
            if content_type == 'ContentCollegeCourse':
                cid = content['subject'] + " " + content['courseCode']
                points[cid] = content['subject']
                links.append((source_id, cid, link_strength))
            
            elif content_type == 'ContentExam':
                cid = content['exam']
                points[cid] = 0
                links.append((source_id, cid, link_strength))
            
            elif content_type == 'ContentOtherCourse':
                cid = content['course']
                points[cid] = 0
                links.append((source_id, cid, link_strength))
        elif node_type == 'CollegeCourse':
            cid = prereq_obj['subject'] + " " + prereq_obj['course_code']
            points[cid] = prereq_obj['subject']
            links.append((source_id, cid, link_strength))
        elif node_type == 'ContentExam':
            cid = prereq_obj['exam']
            points[cid] = 0
            links.append((source_id, cid, link_strength))
        elif node_type == 'ContentOtherCourse':
            cid = prereq_obj['course']
            points[cid] = 0
            links.append((source_id, cid, link_strength))
        
        elif node_type == 'PrerequisiteGroup':
            for child in prereq_obj.get('children', []):
                if prereq_obj.get('logic') == "AND":
                    extract_points_and_links(child, source_id, source_group, link_strength)
                else:
                    extract_points_and_links(child, source_id, source_group, link_strength/2)
        
        # Ignore OtherRequirement, etc.
    
    # elif isinstance(prereq_obj, list):
    #     for item in prereq_obj:
    #         extract_points_and_links(item, source_id, source_group)
            
for prereq_text, prereq_data_list in converted.items():
    course_info = prereq_text_to_course.get(prereq_text)
    
    assert course_info
    
    subject, course_code = course_info
    source_id = subject + " " + course_code
    points[source_id] = subject  # Add the course itself as a point
    
    # data entry is hard
    if type(prereq_data_list) == list:
        true_prereq = prereq_data_list[0]
    else:
        true_prereq = prereq_data_list
    
    prereq_obj = true_prereq['prerequisites']
            
    extract_points_and_links(prereq_obj, source_id, subject, 1)


# Add all subject/course_code pairs from prerequisites to points
# for subject, course_code, _ in prerequisites:
#     cid = subject + " " + course_code
#     if cid not in points:
#         points[cid] = subject

# Write points.csv
with open('data/points.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Group'])
    for cid, group in points.items():
        writer.writerow([cid, group])

# Write links.csv
with open('data/links.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Source', 'Target', 'Value'])
    for source, target, value in links:
        writer.writerow([target, source, value])