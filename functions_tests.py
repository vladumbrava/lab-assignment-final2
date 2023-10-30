import functions as f


def test_add():
    score_list = []
    score_list = f.add(score_list, 50)
    assert len(score_list) == 1


def test_add2():
    score_list = []
    score_list = f.add(score_list, 120)
    assert len(score_list) == 0


def test_add3():
    score_list = []
    score_list = f.add(score_list, 6)
    assert len(score_list) == 0


def test_insert1():
    score_list = []
    index = 0
    value = 10

    result = f.insert_in_score_list(score_list, index, value)

    assert result == [10]


def test_insert_2():
    score_list = [1, 2, 3]
    index = 2
    value = 10

    result = f.insert_in_score_list(score_list, index, value)

    assert result == [1, 2, 10, 3]


def test_insert3():
    score_list = [1, 2, 3]
    index = 2
    value = 5

    result = f.insert_in_score_list(score_list, index, value)

    assert result == [1, 2, 3]


def test_remove1():
    score_list = [1, 2, 3, 4, 5]
    index = 2

    result = f.remove(score_list, index)

    assert result == [1, 2, 4, 5]


def test_remove2():
    score_list = [1, 2, 3, 4, 5]
    index = 2

    result = f.remove(score_list, index)

    assert result is score_list


def test_remove3():
    score_list = [1, 2, 3, 4, 5]
    index = -1

    result = f.remove(score_list, index)

    assert result == score_list


def test_remove_fromIndex1():
    score_list = [1, 2, 3, 4, 5]
    from_index = 1
    to_index = 3

    result = f.remove_fromindex_toindex(score_list, from_index, to_index)

    assert result == [1, 5]


def test_remove_fromIndex2():
    score_list = [1, 2, 3, 4, 5]
    from_index = 1
    to_index = 3

    result = f.remove_fromindex_toindex(score_list, from_index, to_index)

    assert result is score_list


def test_remove_fromIndex3():
    score_list = [1, 2, 3, 4, 5]
    assert f.remove_fromindex_toindex(score_list, -1, 3) == [1, 2, 3, 4, 5]


def test_replace1():
    score_list = [1, 2, 3, 4, 5]
    index = 1
    new_value = 0
    expected_result = [1, 0, 3, 4, 5]

    assert f.replace(score_list, index, new_value) == expected_result


def test_replace2():
    score_list = [1]
    index = 0
    new_value = 0
    expected_result = [0]

    assert f.replace(score_list, index, new_value) == expected_result


def test_replace_returns_modified_list():
    score_list = [1, 2, 3, 4, 5]
    index = -2
    new_value = 60
    score_list = f.replace(score_list, index, new_value)
    assert len(score_list) == 5


def test_sorted_standings1():
    score_list = [10, 5, 8, 3, 7]
    expected_result = ["1st place: 1th participant", "2nd place: 3th participant", "3rd place: 5th participant",
                       "4th place: 2th participant", "5th place: 4th participant"]
    assert f.sorted_standings(score_list) == expected_result


def test_sorted_standings2():
    score_list = []
    expected_result = []
    assert f.sorted_standings(score_list) == expected_result


def test_sorted_standings3():
    score_list = [10, 5, 8, 3, 7, 10]
    expected_result = ["1st place: 1th participant", "2nd place: 6th participant", "3rd place: 3th participant",
                       "4th place: 5th participant", "5th place: 2th participant", "6th place: 4th participant"]
    assert f.sorted_standings(score_list) == expected_result


def test_filter_greater1():
    score_list = []
    value = 10
    assert f.filter_greater(score_list, value) == []


def test_filter_greater2():
    score_list = [1, 2, 3, 4, 5]
    value = 10
    assert f.filter_greater(score_list, value) == []


def test_filter_greater3():
    score_list = [10, 20, 30, 40, 50]
    value = 25
    assert f.filter_greater(score_list, value) == [30, 40, 50]


def test_filter_mul1():
    score_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    value = 3
    assert f.filter_mul(score_list, value) == [3, 6, 9]


def test_filter_mul2():
    score_list = [1, 2, 3, 4, 5]
    value = 2.5
    assert f.filter_mul(score_list, value) == [5]


def test_filter_mul3():
    score_list = [2, 4, 6, 8, 10]
    value = 2
    assert f.filter_mul(score_list, value) == score_list
