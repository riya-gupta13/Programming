def reverseWords(s: str) -> str:
    l=s.split(' ')
    st=[]
    for i in l:
        st.append(i[::-1])
    print(" ".join(st))


s = "God Ding"
# Output: "s'teL ekat edoCteeL tsetnoc"
reverseWords(s)