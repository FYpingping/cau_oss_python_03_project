import file_manager             # file_manager 모듈을 import
import parking_spot_manager     # parking_spot_manager 모듈을 import

def start_process(path):
    str_list = file_manager.read_file(path)                             # 매개로 받은 path로 파일을 읽어 리스트로 변환
    str_list = parking_spot_manager.str_list_to_class_list(str_list)    # 문자열 리스트를 객체 리스트로 변환
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(str_list)                      # 문자열 리스트를 출력
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            """
            select에 입력값에 따른 각각의 경우에 불러오는 함수는 필터링 함수들은
            사용자가 입력한 keyword가 str_list에 포함되어 있을 경우에만 str_list에 새로 저장
            str_list는 참조를 잃고 새로운 객체 리스트를 참조하므로 기존의 객체 리스트는 삭제됨
            """
            if select == 1:
                keyword = input('type name:')
                str_list = parking_spot_manager.filter_by_name(str_list, keyword)
            elif select == 2:
                keyword = input('type city:')
                str_list = parking_spot_manager.filter_by_city(str_list, keyword)
            elif select == 3:
                keyword = input('type district:')
                str_list = parking_spot_manager.filter_by_district(str_list, keyword)
            elif select == 4:
                keyword = input('type ptype:')
                str_list = parking_spot_manager.filter_by_ptype(str_list, keyword)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)                    # 최소,최대의 경도, 위도를 튜플에 저장
                str_list = parking_spot_manager.filter_by_location(str_list, locations)    #범위 내의 위치한 객체들을 저장
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")                       # Exit 출력하고 반복 종료 ( 프로그램 종료 )
            break
        else:
            print("invalid input")