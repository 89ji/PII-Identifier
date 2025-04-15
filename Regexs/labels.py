import re
from typing import *

# Provided a regex for the label, it will remove the content after the colon for that tag.
# Format for the post-colon contents can also be specified.
# The regex for finding the content must contain exactly one match group
# The label regex may contain any amount of match groups
def LabelwiseRemove(tag :str, fullText :str, label :str, content :str = r".*") -> Tuple[str, List[str]]:
    groups = CountMatchGroups(label)

    regex = re.compile(f".*{label}.*: ?({content})", re.I)
    matches = regex.finditer(fullText)
    matchList = []
    for match in matches:
        item = match.group(groups + 1)
        matchList.append(item)
        fullText = fullText.replace(item, tag)
    return (fullText, matchList)


def CountMatchGroups(regex :str) -> int:
    return regex.count("(")


'''
sample = ''''''
Patient Name: Emily Carter
Date of Birth: 11/05/1988
Medical record number:TXB4459-BS34334
SSN: 321-67-8923
Date of Visit: 02/14/2024
Hospital Name: Greenfield Medical Center
''''''

print( LabelwiseRemove("*ssn*", sample, "SSN")[0] )
print( LabelwiseRemove("*dob*", sample, "(dob|Date of birth)")[0] )
fullText, removed = LabelwiseRemove("*hospital*", sample, r"hospital")
print(fullText)
'''