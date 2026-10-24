#15분 36초
#파이썬은 string처리가 쉬운 언어라 문제가 어렵지 않았습니다.
#java는 어려울 듯?..
def solution(data, ext, val_ext, sort_by):
    #code 0, date 1, maximum 2, remain 3
    answer = []
    # print(type(ext))
    cur=0
    sort=0
    #무지성 구현... 더 나은 방법이 있을 것 같다...
    if ext=="code":
        cur=0
    elif ext=="date":
        cur=1
    elif ext=="maximum":
        cur=2
    elif ext=="remain":
        cur=3
    if sort_by=="code":
        sort=0
    elif sort_by=="date":
        sort=1
    elif sort_by=="maximum":
        sort=2
    elif sort_by=="remain":
        sort=3
    
    #비교 보다 더 작으면
    for i in data:
        if(int(i[cur])<val_ext):
            answer.append(i)
    # sorted해서 lambda식 기준으로 sort sorted를 사용하면 return 값이 sort되는거라 return값을 꼭 받아야함
    result=sorted(answer,key=lambda x:x[sort])
    
    
    return result
