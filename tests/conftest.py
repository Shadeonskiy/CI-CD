import os
import pytest


@pytest.fixture(autouse=True)
def prepare_text_files(tmp_path):
    target_file1 = os.path.join(tmp_path, 'test1.txt')
    with open(target_file1, 'w') as file:
        lines = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n',
                 'Fusce eu commodo arcu. Phasellus imperdiet convallis turpis.\n'
                 ]
        file.writelines(lines)

    target_file2 = os.path.join(tmp_path, 'test2.txt')
    with open(target_file2, 'w') as file:
        lines = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n',
                 'Phasellus imperdiet convallis turpis.\n',
                 'Fusce eu commodo arcu.\n'
                 ]
        file.writelines(lines)
    return target_file1, target_file2
