Usage:

if example json is:
```json
{
    "school_name": "Dunder Miflin",
    "class": "Year 1",
    "students": [
    {
        "id": "A1",
        "name": "Jim",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {
        "id": "A2",
        "name": "Dwight",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {
        "id": "A3",
        "name": "Kevin",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}
```

```shell
$ readpl test* 
test.json: school_name=Dunder Miflin
test.json: class=Year 1
test.json: students/[0]/id=A1
test.json: students/[0]/name=Jim
test.json: students/[0]/math=60
test.json: students/[0]/physics=66
test.json: students/[0]/chemistry=61
test.json: students/[1]/id=A2
test.json: students/[1]/name=Dwight
test.json: students/[1]/math=89
test.json: students/[1]/physics=76
test.json: students/[1]/chemistry=51
test.json: students/[2]/id=A3
test.json: students/[2]/name=Kevin
test.json: students/[2]/math=79
test.json: students/[2]/physics=90
test.json: students/[2]/chemistry=78 
```
