# Langara Prerequisites -> Data

This is a project to parse course prerequisites from Langara College in text form to data.

This has been completed, and you can find the parsed data in `data/converted.json`.

Approximately 9% (51/564) of prerequisites could not be parsed due to:
1) contained prerequisites not captured by my data schema (e.g. gpa requirement or enrollment in a degree)
2) ambiguous text (ie a *and* b *or* c)
You can find unparsed cases in `data/hard_cases.py`

Although an LLM was used to parse text, all conversions were approved by a human. It is important to note that although I have made a best effort, there is no guarantee of all data being correct. The only source of truth is Langara's student information system.

Do however note that there may be inconsistency in some of the data formatting, particularly with `OtherRequirement` nodes.

Please read `instructions.md` to learn about the data schema.



Known issues:
- `EquivalentCourse` is used inconsistently.
- In cases where a grade isn't specifically stated, we try to use a grade previously seen in the text. This may mean that some courses are listed as needing a `C-`/`C` instead of Completion.
- Corequisites are not listed here (notably with MATH 1173/1183) due to data issues.
- Due to changes in the Langara website breaking my scraper, the given prerequisite texts are from ~May 2025.

