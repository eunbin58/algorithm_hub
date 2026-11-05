def solution(new_id):
    #1단계
    new_id=new_id.lower()
    #2단계
    nnew_id=''
    for i in new_id:
        if(i=='.' or 'a' <= i <= 'z'or '0' <= i <= '9' or i=='-' or i=='_'):
            nnew_id+=i
    # print(nnew_id)
    #3단계
    new_id=''
    for i in range(len(nnew_id)):
        if(i==len(nnew_id)-1):
            new_id+=nnew_id[i]
            break
        elif(nnew_id[i+1]=='.' and nnew_id[i]=='.'):
            continue
        new_id+=nnew_id[i]
    # print(new_id)
    #4단계
    if(new_id[0]=='.'):
        new_id=new_id[1:]
    # print(len(new_id))
    if(len(new_id)!=0 and new_id[-1]=='.'):
        new_id=new_id[:len(new_id)-1]
    # print(new_id)
    
    #5단계
    
    if(len(new_id)==0):
        new_id+='a'
    # print(new_id)
        
    #6단계
    if(len(new_id)>=16):
        new_id=new_id[:15]
        if(new_id[-1]=='.'):
            new_id=new_id[:len(new_id)-1]
    # print(new_id)
    #7단계
    if(len(new_id)<=2):
        while len(new_id)<3:
            new_id+=new_id[-1]
    return new_id