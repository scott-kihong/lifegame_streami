Game of life 
======

## Overview

Game of life를 구현하기 위해 총 네 개의 클래스를 구분하여 작성하였음

[Files]
- cell.py : grid의 하나하나의 요소로써 자신의 상태를 설정하고 상태를 반환하는 역할을 수행
- grid.py : 게임 실행에 필요한 일종의 보드판으로 보드를 생성하고 초기화하며 게임에 필요한 로직이 작성되어 있음
- grid_file_readwriter.py : 사용자로부터 파일로써 초기 설정 값을 입력 받았을 경우 파일을 읽어들여 초기화 하거나, 특정 단계의 상태를 저장하는 역할을 하고 있음
- grid_viewer.py : grid에 저장 되어있는 cell 인스턴스의 상태값을 읽어들여 특정한 기호로 출력하는 작업을 구현
- constants.py : 구현에 있어서 필요한 상수를 정의
- exception.py : 구현에 있어서 필요한 예외를 정의

[Directory]
- generation_files : 사용자 지정 초기화 파일
- generation_dumps : 특정 generation stage에서 덤프를 할 경우 본 디렉토리로 파일을 저장함 (format : gen_{n_generation}.txt)

## How to run

1. git clone https://github.com/scott-kihong/lifegame_streami.git
2. cd lifegame_streami
3. Run game!
    - python main.py
    - python main.py generation_files/plus.txt
    - python main.py generation_files/plus.txt {n_generation}
