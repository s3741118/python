# import streamlit
# # st = streamlit.header("this is my form")
# # st = streamlit.form(form1)

# st = streamlit.set_page_config(page_icon="meo.ico",page_title="phimmoi")
# st = streamlit.title("danh sach phim")

# # userName = streamlit.text_input(label="ten dang nhap")
# # UserPW = streamlit.text_input(label="mat khau", type="password")
# # def signUp():
# #     f = open(userName+".txt", "w")
# #     f.write(UserPW)
# #     f.close()

# # st = streamlit.button(label="save", on_click=signUp)
# def page1():
#     st = streamlit.video("ai muon nghe khong.mp4")
#     st = streamlit.caption("ai muon nghe khong")
#     f = open("ai muon nghe khong.mp4", "rb")
#     st = streamlit.download_button(label="tai video", data= f, file_name="ai muon nghe khong.mp4")

#     st = streamlit.video("di ve nha.mp4")
#     st = streamlit.caption("di ve nha")
#     f = open("di ve nha.mp4", "rb")
#     st = streamlit.download_button(label="tai video", data= f, file_name="di ve nha.mp4")

# def page2():
#     st = streamlit.video("loi nho.mp4")
#     st = streamlit.caption("loi nho")
#     f = open("loi nho.mp4", "rb")
#     st = streamlit.download_button(label="tai video", data= f, file_name="loi nho.mp4")
# # def page2():
# #     st = streamlit.write("new page")
# page_menu = {
#     "Page 1": page1,
#     "Page 2": page2,
# }
# select_page = streamlit.selectbox("select a page",page_menu.keys())
# page_menu[select_page]()

# # st = streamlit.file_uploader()

import streamlit

st = streamlit.set_page_config(page_icon="meo.ico",page_title="phimmoi")
st = streamlit.title("Hellu LANH")
st = streamlit.title("Duoi day la danh sach nhac va phim")

st = streamlit.video("ai muon nghe khong.mp4")
st = streamlit.caption("ai muon nghe khong")
f = open("ai muon nghe khong.mp4", "rb")
st = streamlit.download_button(label="tai video", data= f, file_name="ai muon nghe khong.mp4")

st = streamlit.video("di ve nha.mp4")
st = streamlit.caption("di ve nha")
f = open("di ve nha.mp4", "rb")
st = streamlit.download_button(label="tai video", data= f, file_name="di ve nha.mp4")
st = streamlit.video("loi nho.mp4")
st = streamlit.caption("loi nho")
f = open("loi nho.mp4", "rb")
st = streamlit.download_button(label="tai video", data= f, file_name="loi nho.mp4")

