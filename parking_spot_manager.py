class parking_spot:

    def __init__(self, name, city, district, ptype, longitude, latitude):   # 주차장 객체를 만들기 위한 생성자
        self.__item = { 'name':name,                        # 이름
                        'city':city,                        # 도시
                        'district':district,                # 구역
                        'ptype':ptype,                      # 주차장 타입
                        'longitude':float(longitude),       # 경도 float 타입
                        'latitude':float(latitude)}         # 위도 float 타입의 원소들을 딕셔너리에 저장
        
    def get(self, keyword = 'name'):                        # 클래스의 객체 딕셔너리 getter 메소드
        return self.__item[keyword]

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

"""
매개변수로 받는 문자열을 컴마로 구분지은 후 각 정보를 통해 객체를 생성
매개변수 리스트의 길이만큼의 반복을 통해 생성된 객체들을 리스트에 추가
반복이 끝나면 객체들의 리스트를 반환 즉, 객체 리스트를 생성하는 함수
"""
def str_list_to_class_list(str_list):   # 매개변수 str_list는 문자열 리스트
    my_object_list= []                  # 객체를 담을 리스트 my_object_list
    for s in str_list:                  # str_list의 길이만큼 반복
        my_list = s.split(',')          # 리스트의 원소들을 컴마 기준으로 split해서 my_list 리스트에 저장
        my_object = parking_spot(my_list[1], my_list[2], my_list[3], my_list[4], my_list[5], my_list[6])
        my_object_list.append(my_object)       # my_list에 담긴 정보로 객체를 생성한 my_object를 my_object_list에 추가
    return my_object_list               # 객체 리스트 반환

"""
매개변수로 객체 리스트를 받으며 받은 리스트의 길이를 출력
객체 리스트의 길이만큼 반복하여 객체의 딕셔너리를 문자열로 출력
"""
def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for spot in spots:
        print(str(spot))


"""
filter 함수들
각각의 함수는 자원명, 시도, 시군구, 주차장 유형, 위치( 경도, 위도 )에 따라 필터링하는 함수
각각의 함수는 매개변수로 객체 리스트와 각각 필요한 데이터를 받음
객체 리스트의 길이만큼 리스트 함축으로 반복을 시행하는데, 인자로 받은 문자열이 해당하는 딕셔너리 value 값에
포함이 된다면 각각 새로운 객체 리스트에 저장하고 반환한다.
"""

def filter_by_name(spots, name):
    name_filtered_list = [i for i in spots if name in i.get('name')]
    return name_filtered_list

def filter_by_city(spots, city):
    city_filtered_list = [i for i in spots if city in i.get('city')]
    return city_filtered_list

def filter_by_district(spots, district):
    district_filtered_list = [i for i in spots if district in i.get('district')]
    return district_filtered_list

def filter_by_ptype(spots, ptype):
    ptype_filtered_list = [i for i in spots if ptype in i.get('ptype')]
    return ptype_filtered_list

"""
위치를 필터링 하는 함수.
인자로 받은 spots 객체 리스트의 원소 중에서 locations 튜플의 인자로 받은 최소, 최대의 경도, 위도 범위 안에 위치하는
객체들을 새로운 객체 리스트를 생성해서 반환
"""
def filter_by_location(spots, locations):
    location_filtered_list = [i for i in spots \
                              if locations[0] < i.get('latitude') and i.get('latitude') < locations[1] \
                                        and locations[2] < i.get('longitude') and i.get('longitude') < locations[3]]
    return location_filtered_list

"""
인자로 받은 키워드를 객체의 딕셔너리의 키에 전달하고
그것을 토대로 올림차순으로 정렬하고 새로운 리스트로 반환하는 함수
"""
def sort_by_keyword(spots, keyword):
    return sorted(spots, key = lambda x:x.get(keyword))         # 딕셔너리 정렬 참고 https://bio-info.tistory.com/115



# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)