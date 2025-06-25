hard_cases = [
    
    # missing information
    'Prerequisite(s): Successful completion of Term Two courses.',
    'Prerequisite(s): Successful completion of Term One courses.', 
    
    # ambiguous
    'Prerequisite(s): A minimum "C" grade in EXPE 4800 or EXPE 4801, 4802, and 4803.',   
    
    # Year standing??? or is it course reqs?
    'Prerequisite(s): Completion of the third year of the Bachelor of Science in Bioinformatics; and a minimum "C-" grade in COOP 2501.',
    
    # since when did langara have crosslisting???
    'Prerequisite(s): PCCN 1201 (POLI 1145) or 1202.',
    
    'Prerequisite(s): A minimum "C-" grade in HKIN/KINS 1190 (KINS 1190 and 2361 may be taken concurrently).',
    
    # we can't calculate gpa
    'Prerequisite(s): A minimum "C" grade in BUSM 2300, COOP 2300, or EXPE 2300; a minimum 2.6 GPA; acceptance to the co-operative education option; and confirmed co-op work placement.',
    
    'Prerequisite(s): A minimum "C" grade in BUSM 1310, 2300, COOP 2300, or EXPE 2300; a minimum 2.6 GPA; acceptance to the co-operative education option; and an approved co-op work placement.',
    
    'Prerequisite(s): A minimum "C" grade in BUSM 1310, BUSM 2300, COOP 2300, or EXPE 2300; a minimum 2.6 GPA; acceptance to the co-operative education option; an approved co-op work placement; and successfull completion of COOP 2302.',
    
    # so ambiguous
    'Prerequisite(s): A minimum "C" grade in EXPE 4800; or EXPE 4801, 4802, and 4803; acceptance to the co-op option; and confirmed co-op work placement.',
    
    # two of the following... pain
    'Prerequisite(s): A minimum "C" grade in all of the following: APPL 5110 and 5130; and two of the following: APPL 5210, 5220, 5230, or 5240.',
    
    'Prerequisite(s): A minimum "C" grade in two of: CPSC 1160, 1181, or 1280.',
    
    'Prerequisite(s): A minimum "C-" grade in all of the following: three credits of AHIS; FINA 1120, 1131, and 1161; and three of the following: FINA 1142, 1143, 1171, or 1220.',
    
    # uh oh, there's quite a few of these
    'Prerequisite(s): A minimum "C-" grade in all of the following: one of the following: AHIS 1112, 1114, 1212, 1214, 1301, or 1302; and four of the following: FINA 1111, 1131, 1142, 1143, 1171, or 1220; and FINA 1120 and 1161.',
    
    'Prerequisite(s): A minimum "C-" grade in all of the following: three credits of AHIS; four of the following: FINA 1111, 1131, 1142, 1171, or 1220; and FINA 1120 and 1161.',
    
    'Prerequisite(s): Any two of the following with a minimum "C-" grade: BIOL 1115, 1118, 1215, 1218; CHEM 1117, 1217, 1120; GEOG 1155, 1190; GEOL 1107, or 1110; or permission of the environmental studies coordinator.',
    
    'Prerequisite(s): A minimum "C-" grade in all of the following: three credits of AHIS; three of the following: FINA 1111, 1131, 1142, 1171, or 1220; and FINA 1120, 1143, and 1161.',
    
    'Prerequisite(s): A minimum "C-" grade in all of the following: three credits of AHIS; FINA 1111, 1120, and 1161; and three of the following: FINA 1131, 1142, 1171, or 1220.',
    
    'Prerequisite(s): A minimum "C" grade in two of: BIOL 2315, 2330, or 2415; and a minimum "C" grade in CPSC 1150 or 1155.',
    
    'Prerequisite(s): A minimum "C-" grade in all of the following: one of the following: AHIS 1112, 1114, 1212, 1214, 1301, or 1302; three of the following: FINA 1111, 1131, 1142, 1143, or 1220; and FINA 1120, 1161, and 1171.',
    
    'Prerequisite(s): A minimum "C-" grade in all of the following: one of the following: AHIS 1112, 1114, 1212, 1214, 1301, or 1302; FINA 1111, 1120, and 1161; and three of the following: FINA 1131, 1142, 1143, 1171, or 1220.',
    
    'Prerequisite(s): A minimum "C-" grade in all of the following: one of the following: AHIS 1112, 1114, 1212, 1214, 1301, or 1302; three of the following: FINA 1111, 1131, 1143, 1171, or 1220; and FINA 1120, 1142, and 1161.',
    
    # oh no course conflicts are unaccounted for
    # Processing: Prerequisite(s): Grade 12 Spanish; or a minimum "C+" grade in SPAN 1215 or 1218. May not be taken concurrently with SPAN 1118.
    
    # also the short prereqs are unaccounted for
    
    # this is clearly a departmental override
    # not sure what to do with it though
    'Prerequisite(s): A minimum "C-" grade in MATH 2362 or 1252 and 2371. With permission, one of MATH 2362, 1252, or 2371 may be taken concurrently.',
    
    # too many and/ors and the llm will give up
    'Prerequisite(s): A minimum "C-" grade in one of the following: MATH 1271, 1273, 1274, or 1275; or a minimum "A" grade in MATH 1171, 1173, or 1253 and concurrent registration in one of the following: MATH 1271, 1273, 1274, or 1275. Prerequisites are valid for only three years.',
    
    'Prerequisite(s): A minimum "C" grade in all of the following: AHIS 1212 or 1219; BUSM 1902; JOUR 1168 or PHOT 2320; PHOT 2305, 2310, 2325, 2420, 2425; PHOT 2440 or 2441; PHOT 2490; and PUBL 1100 or 1900. ( BUSM 1902, PHOT 2425 and 2490 may be taken concurrently).',
    
    # llm can't put that many words into Other
    'Prerequisite(s): A minimum "C-" grade in PSYC 1115 and 1215. Prerequisites waived for students admitted to the Early Childhood Education or the Education Assistant programs.',
    
    'Prerequisite(s): A minimum "C-" grade in PSYC 1115 and 1215. Prerequisites waived for students admitted to the early childhood education or the special education assistant programs.',
    
    
    # AMBIGUITY HELL:
    
    # unclear *which* may be taken concurrently
    'Prerequisite(s): A minimum "C" in one of the following: AHIS 1112, 1212, 1219, DSGN 1100, 1151, 1200, FINA 1120, FLMA 1170, JOUR 1168, PHOT 1100, 1105, PUBL 1100, 1190, THEA 1110, or WMDD 4800 (may be taken concurrently)',
    
    # which can be taken concurrently??
    'Prerequisite(s): A minimum "C-" grade in PHYS 1215 or 1225; and one of the following: MATH 1271, 1273, 1274, or 2371 (may be taken concurrently); or permission of department.',
    
    # same problem
    'Prerequisite(s): A minimum "C" in one of the following: AHIS 1112, 1212, 1219, DSGN 1100, 1151, 1200, FINA 1120, FLMA 1170, JOUR 1168, PHOT 1100, 1105, PUBL 1100, 1190, THEA 1110, or WMDD 4800 (may be taken concurrently).',
    
    # unclear whether C applies to the six UT credits
    'Prerequisite(s): Completion of a minimum 54 credits including a minimum "C" grade in CMNS 2228, MARK 1115, and six credits of university-transferable English or communications.',
    
    # unclear what the C applies to
    'Prerequisite(s): Completion of a minimum 54 credits including a minimum "C" grade in BUSM 2200 or INTB 2000, CMNS 2228, and six credits of university-transferable English or communications.',
    
    # unclear if this is the MDT or SDT
    'Prerequisite(s): A minimum "C+" grade in PSYC 1115 and 1215; and one of the following: a minimum "C" grade in Foundations of Mathematics 11, Pre-calculus 11, Foundations of Mathematics 12, or Pre-calculus 12; an "S" grade in MATH 1150; or a satisfactory score (053) on the statistics version of the Mathematics and Statistics Diagnostic Test (MDT).',
    
    # not actually required... or not??
    'Prerequisite(s): KINS 1151 relies on a basic knowledge of high school math principles (basic algebra, trigonometry). Students without a minimum "B" grade in Principles of Math 11 (PM11) or a minimum "C+" grade in PM 12, or a score of 70 on the Langara Math Diagnostic Test, should strongly consider taking MATH 1150 prior to this course.',
    
    # unclear what the permission overrides
    'Prerequisite(s): A minimum "C-" grade in all of the following: GERO 1100, 1115, 1215, and 1300; and an "S" grade in GERO 1816 and 1916; or permission of the program coordinator.',
    
    # unclear what credits are in the bachelor
    'Prerequisite(s): Successful completion of at least 105 credits in the Bachelor of Business Administration including a minimum "C" grade in BUSM 4200 and CMNS 2228; and an "S" grade in BUSM 3000 or a minimum "C-" grade in COOP 2301. This course is restricted to students in their final term of the Bachelor of Business Administration.',
    
    # or / and ambiguity
    'Prerequisite(s): A minimum "C" grade in BIOL 2315, 2330, CPSC 2150, 3260, and STAT 3225; and a minimum "C" grade in MATH 1252 or 2362 and 2382.',
    
    
    # information not provided:
    'Prerequisite(s): An "S" grade in FSRV 1219 and 2429; a minimum "C" grade in FSRV 4323, NUTR 2322, and 2422; a minimum "C" grade in BUSM 1500, CMNS 1115, or 2228; a minimum "C" grade in CMNS 1118, ENGL 1123, or 1127; and a minimum "C-" in all other program courses.',
    
    'Prerequisite(s): All of the following: an "S" grade in FSRV 1219 and 2429; a minimum "C" grade in FSRV 4323, NUTR 2322, and 2422; a minimum "C" grade in BUSM 1500, CMNS 1115, or 2228; a minimum "C" grade in CMNS 1118, ENGL 1123, or 1127; and a minimum "C-" grade in all other program courses.',
    
    # idk
    'Prerequisite(s): A minimum "C" grade in all 1000 and 2000 level Recreation courses (or an "S" in courses graded S/U).',
    
    # maybe we need a degree specific thing... idk
    # probably stretching the scope WAY TOO MUCH
    # need to set achievable goals..................
    'Prerequisite(s): A minimum "C-" grade in PSYC 1115 and 1215. Prerequisites waived for students enrolled in the early childhood education or education assistant programs.',
    
    # intb 200........
    'Prerequisite(s): Completion of a minimum 54 credits including a minimum "C" grade in CMNS 2228, INTB 200, and six credits of university-transferable English or communications with a minimum "C" grade.',
    
    # i wasn't aware we had year standings...
    'Students must be in at least second year of the Bachelor of Business Administration, or be in second-year arts and sciences with departmental approval.',
    
    # what is "in the bba"
    'Prerequisite(s): Successful completion of a minimum of 90 credits in the BBA; a minimum "C" grade in CMNS 2228; a minimum "C" grade in six additional credits of university-transferable English or communications; and BUSM 3000, COOP 2301, or 2303.',
    
    #ambiguous and/or
    'Prerequisite(s): Acceptance to the co-op option; an approved co-op work placement; and successful completion of COOP 3301 or COOP 3302 and 3303.',
    
    # confusing
    'Prerequisite(s): Before registering in this course, a student should have completed a second-year college Chinese course or equivalent, e.g. completion of six years of elementary school or more in China or Taiwan, and know about 2000 Chinese characters.',
    
    # they added a comma
    'Prerequisite(s): Before registering in this course, a student should have completed a second-year college Chinese course or equivalent, e.g., completion of six years of elementary school or more in China or Taiwan, and know about 2000 Chinese characters.',
    
    'Prerequisite(s): Students who have not completed CHIN 3331 should consult an instructor of Chinese before registering in this course. Students should have already completed at least a  second-year college Chinese course or equivalent, e.g., completion of six years of elementary school or more in China or Taiwan,  and know about 2000 Chinese characters.',
    
    # final year of BRM program
    'Prerequisite(s): Completion of a minimum of 90 credits including a minimum "C" grade in six credits of university-transferable English or communications; or permission of the department. Students must be in their final year of the BRM Program and have a minimum "C" grade in BUSM 4200. BUSM 4200 may be taken concurrently with RECR 4300.',
    
    # what does second year mean??
    'Prerequisite(s): Students must be in at least second year of the Bachelor of Business Administration, or be in second-year arts and sciences with departmental approval.',
    
    # idk how to represent this in data 
    'Prerequisite(s): Completion of a minimum of 54 credits including a minimum "C" grade in MARK 1115; and a minimum "C" grade in six credits of university-transferable English or communications. For students in the fourth term of the Diploma in Design Formation, a minimum "C" grade in DDSN 2152, MARK 1115, and six credits of university-transferable English or communications will be deemed to be equivalent to the above.',
    
    # what is a CDT??
    'Prerequisite(s): A minimum "B" grade in Chemistry 12 or equivalent; a minimum "C+" grade in CHEM 1118; or CDT results for CHEM 1120; and a minimum "C" grade in Precalculus 12, MDT 75, or MATH 1152. Prerequisites are only valid for three years.',
    
    # who is taking this course???
    'Prerequisite(s): Speaker of English as a first language and a Langara English Test score of LETN 02 or by permission of the English department. If you have an LPI score of 22, please contact the English department chair for correct placement.',
    
    # we lost some prerequisite text
    # so we cannot parse this
    'Prerequisite(s): One of the following: LET 3 (or LPI equivalent); LEAP 8; a minimum "C+" grade in BC English 12, BC English Studies 12, BC Literary Studies 12, or BC English First Peoples 12; a minimum "C-" grade in three credits of university-transferable English or communications; or a minimum "C" grade in ENGL 1120; or an "S" grade in ENGL 1107, 1108, or 1110; and',
]
