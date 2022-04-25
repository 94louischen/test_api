import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(root_dir)

conf_test_dir = os.path.join(root_dir, 'config', 'conf_test.cfg')

conf_uat_dir = os.path.join(root_dir, 'config', 'conf_uat.cfg')

conf_prod_dir = os.path.join(root_dir, 'config', 'conf_prod.cfg')

globe_conf_dir = os.path.join(root_dir, 'config', 'globe_conf.cfg')

report_dir = os.path.join(root_dir, 'output', 'report')

data_dir = os.path.join(root_dir, 'data')

log_dir = os.path.join(root_dir, 'log')

testImg_dir = os.path.join(root_dir, 'data', 'img.jpg')

database_dir = os.path.join(root_dir, 'data', 'database.yaml')

excel_import_dir = os.path.join(root_dir, 'data', 'infra_cases_test.xlsx')