abc="""{
{
  "name":"大学语文{{courseName}}",
  "desc":"大学英语课程",
  "display_idx":""
}
"""

efg="""{
{
  "name":"大学语文",
  "desc":"大学英语课程",
  "display_idx":""
}
"""

print(abc.replace('{{courseName}}','999999999'))
print(efg.replace('{{courseName}}','999999999'))

