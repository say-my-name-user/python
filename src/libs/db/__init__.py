def map_data_with_columns(data, columns):
    result_list = []

    for row in data:
        mapped_dict = {}

        for i in range(len(row)):
            mapped_dict[columns[i]] = row[i]

        result_list.append(mapped_dict)

    return result_list
