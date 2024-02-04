def solution(data, ext, val_ext, sort_by):

    index_map = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ext_index = index_map[ext]
    sort_by_index = index_map[sort_by]

    filtered_data = [item for item in data if item[ext_index] < val_ext]

    sorted_data = sorted(filtered_data, key=lambda x: x[sort_by_index])

    return sorted_data