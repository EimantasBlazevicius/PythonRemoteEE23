import user_data_pr


def test_prepare_data(mock_file, test_list_42):
    with open(mock_file, 'r') as f:
        prepared_data = user_data_pr.prepare_data(f)

    assert prepared_data == test_list_42


def test_filter_underage(test_list_42, test_list_13):
    assert user_data_pr.filter_underage(test_list_42) == test_list_42
    assert user_data_pr.filter_underage(test_list_13) == []
