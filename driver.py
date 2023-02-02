from json import load
from sys import argv, exit
from subprocess import Popen, PIPE


# 입력 받은 인자 설정.
if len(argv) < 3:
    print('driver:', '인자를 찾을 수 없습니다.', '프로그램을 실행하려면 다음 명령을 입력하세요.')
    print('\t', 'python3 driver.py <문제 번호> [python]')
    exit()
else:
    quiz_id = argv[1]
    src_type= argv[2]


# 문제 별 기본 경로, 언어 별 코드 파일 경로 설정.
with open('./path.json', 'r') as f:
    json_data = load(f)
    quiz_dirs = json_data['quiz_dir']
    src_paths = json_data['src_path']

if quiz_id not in quiz_dirs:
    print('driver:', f'{quiz_id} 문제의 경로가 정의되지 않았습니다.')
    exit()
else:
    quiz_dir = quiz_dirs[quiz_id]

if src_type not in src_paths:
    print('driver:', f'{src_type} 형식의 코드가 정의되지 않았습니다.')
    exit()
else:
    src_path = src_paths[src_type]

target_example_path = f'./{quiz_dir}/examples.json'
target_src_path = f'./{quiz_dir}/{src_path}'


# 문제 예제 설정.
with open(f'{target_example_path}', 'r') as f:
    json_data = load(f)
    examples = json_data['examples']


# 코드 형식 type에 따라 소스 코드 src를 실행합니다.
def run(src, type, input):
    if type == 'python':
        p = Popen(['python3', src], stdin=PIPE, stdout=PIPE)
        return p.communicate(input=args)[0].decode('utf-8')


# 소스 코드 실행.
example_id = 0
for example in examples:
    # 입출력, 인자 설정.
    example_id += 1
    inputs = example['input']
    outputs = example['output']
    expected_output = [str(elem) for elem in example['output']]
    args = str.encode('\n'.join(map(str, inputs)))
    test_output = run(target_src_path, src_type, args).split('\n')
    test_output = [o for o in test_output if o]

    # 실행 결과 출력.
    test_result = (expected_output == test_output)
    print('=====', 'example', example_id, '=====')
    print('input:', inputs)
    print('expected output:', expected_output)
    print('test output:', test_output)
    print('test result:', 'success' if test_result else 'failure')
    print('\n')
