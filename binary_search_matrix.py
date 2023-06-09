def binary_search_outer(low, high, array, x):
    if high >= low:
        mid = (low + high) // 2
        return binary_search_inner(0, len(array[mid]) - 1, mid, array, array[mid], x)
    else:
        return "Element doesn't appear in the array"


def binary_search_inner(low, high, outer_mid, full_array, inner_array, x):
    if high >= low:
        inner_mid = (low + high) // 2
        if inner_array[inner_mid] == x:
            return f"[{outer_mid}][{inner_mid}]"

        elif x >= inner_array[0] and x <= inner_array[-1]:
            if inner_array[inner_mid] < x:
                return binary_search_inner(inner_mid + 1, high, outer_mid, full_array, inner_array, x)
            elif inner_array[inner_mid] > x:
                return binary_search_inner(low, inner_mid - 1, outer_mid, full_array, inner_array, x)

    if x < inner_array[0]:
        return binary_search_outer(0, outer_mid - 1, full_array, x)

    else:
        return binary_search_outer(outer_mid + 1, len(full_array) - 1, full_array, x)


mm = [[1, 4, 4, 13, 17, 22, 27, 28], [36, 38, 39, 41, 43, 44, 49], [51, 58, 62, 63, 67]]
print(binary_search_outer(0, len(mm) - 1, mm, 93))
