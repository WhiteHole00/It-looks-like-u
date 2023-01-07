import sqlite3


def SaveAccount():
    user = input("페이스북 이메일 또는 전화번호를 적어주세요 : ")
    pw = input("페이스북 비밀번호를 입력해주세요 : ")
    try:
        con = sqlite3.connect("./db/db.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM main WHERE username == ?;", (user,))
        register = cur.fetchone()
        con.close()
        if register == None:
            con = sqlite3.connect("./db/db.db")
            cur = con.cursor()
            cur.execute("INSERT INTO main VALUES(?, ?, ?);", (user, pw,"O"))
            con.commit()
            con.close()
            return print("계정 등록이 성공적으로 완료 되었습니다.\n프로그램을 껐다 켜 주세요")
        else:
             return print("계정 등록을 실패 하였습니다.\n사유 : 이미 등록 되어 있음")
    except Exception as e:
        print(e)
        return print("오류 발생")
