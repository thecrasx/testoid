

class SortQuestions:
    def __getFirstCharValue(list_: list) -> int:
        for c in list_:
            if c != ' ':
                return ord(c.lower())





    def __merge(list_1: list, list_2: list) -> list:
        len_1 = len(list_1)
        len_2 = len(list_2)

        out = []

        i,j = 0, 0 


        while i < len_1 and j < len_2:
            if SortQuestions.__getFirstCharValue(list_1[i]) < SortQuestions.__getFirstCharValue(list_2[j]):
                out.append(list_1[i])
                i += 1

            elif SortQuestions.__getFirstCharValue(list_1[i]) > SortQuestions.__getFirstCharValue(list_2[j]):
                out.append(list_2[j])
                j += 1

            else:
                out.append(list_1[i]) 
                out.append(list_2[j])

                i += 1
                j += 1

        if i < len_1:
            for x in range(i, len_1):
                out.append(list_1[x])

        elif j < len_2:
            for x in range(j, len_2):
                out.append(list_2[x])


        return out





    def __mergeSort(_list: list) -> list:
        if len(_list) == 1:
            return _list
        
        mid = len(_list) // 2
        left = _list[:mid]
        right = _list[mid:]
        
        return SortQuestions.__merge(
            SortQuestions.__mergeSort(left),
            SortQuestions.__mergeSort(right)
        )





    def sort(_list: list) -> list:
        return SortQuestions.__mergeSort(_list)



if __name__ == "__main__":
    import json

    with open("./Tests/questions.json") as f:
        data = json.load(f)
        data = data["questions"]


    list_ = [x for x in data]


    sorted = SortQuestions.sort(list_)


    for q in sorted:
        print(q)