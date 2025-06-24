def print_prerequisite_node(node:dict[dict | str] | None, indent=0): # type: ignore
    spaces = "  " * indent
    if node is None:
        print(f"{spaces}No prerequisites.")
        return
    
    if 'prerequisites' in node:
        print_prerequisite_node(node['prerequisites'])
        return

    node_type:str = node.get("type") # type: ignore
    
    # Handle PrerequisiteGroup
    if node_type == "PrerequisiteGroup":
        logic = node.get("logic") # type: ignore
        print(f"{spaces}Group ({logic}):")
        
        for child in node.get("children", []): # type: ignore
            print_prerequisite_node(child, indent + 1)

    # Handle ContentScoreRequirement
    elif node_type == "ContentScoreRequirement":
        content = node.get("content", {})
        score = node.get("score", {})
        content_type = content.get("type")
        score_str = ""
        if score.get("type") == "ScoreLetter":
            score_str = f'minimum "{score.get("minGrade")}"'
        elif score.get("type") == "ScorePercentage":
            score_str = f'minimum {score.get("minPercent")}%'
        elif score.get("type") == "ScoreExam":
            score_str = f'score {score.get("minScore")}'
        elif score.get("type") == "ScoreLiteral":
            score_str = f'score "{score.get("score")}"'
        elif score.get("type") == "ScoreCompletion":
            score_str = "completion"

        if content_type == "ContentCollegeCourse":
            subj = content.get("subject")
            code = content.get("courseCode")
            conc = content.get("canBeTakenConcurrently", False)
            conc_str = " (may be taken concurrently)" if conc else ""
            print(f'{spaces}{subj} {code}{conc_str} ({score_str})')
        elif content_type == "ContentOtherCourse":
            print(f'{spaces}{content.get("course")} ({score_str})')
        elif content_type == "ContentExam":
            print(f'{spaces}{content.get("exam")} ({score_str})')
        elif content_type == "ContentCollegeCredits":
            subject = content.get("subject")
            credits = content.get("credits")
            year = content.get("year")
            ut = content.get("universityTransferable", False)
            subj_str = "any course" if subject is None else ", ".join(subject)
            year_str = f", year {year}" if year else ""
            ut_str = "UT " if ut else ""
            print(f'{spaces}{credits} credits of {ut_str}{subj_str}{year_str} ({score_str})')
        elif content_type == "ContentCollegeCompletedCourses":
            subjects = content.get("subjects")
            year = content.get("year")
            ut = content.get("universityTransferable", False)
            subj_str = "any subject" if subjects is None else ", ".join(subjects)
            year_str = f", year {year}" if year else ""
            ut_str = "UT " if ut else ""
            print(f'{spaces}Completed courses in {ut_str}{subj_str}{year_str} ({score_str})')
        else:
            print(f'{spaces}Unknown ContentScoreRequirement: {content} ({score_str})')

    # Handle ContentCollegeCourse (not wrapped in ContentScoreRequirement)
    elif node_type == "ContentCollegeCourse":
        subj = node.get("subject")
        code = node.get("courseCode")
        conc = node.get("canBeTakenConcurrently", False)
        conc_str = " (may be taken concurrently)" if conc else ""
        print(f'{spaces}{subj} {code}{conc_str}')

    # Handle OtherRequirement
    elif node_type == "OtherRequirement":
        print(f'{spaces}Other: {node.get("note")}')

    else:
        print(f'{spaces}Unknown node type: {node_type}')


def print_human_readable(node: dict | None):
    print_prerequisite_node(node)