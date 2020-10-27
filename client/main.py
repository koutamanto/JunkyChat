import sys, json, requests
from datetime import datetime
from PyQt5 import QtWidgets, QtCore
from JunkyChat import Ui_Dialog
from PyQt5.QtCore import QUrl

user_name = "ゲスト"#1.ここのユーザー名を変更する
#2.「py main.py」で起動する 3.メッセージを入力する 4.話す
#エラーが出たら「pip install requests」のように「pip install エラーに表示されているモジュール名」でインストールする

class Test(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
    super(Test, self).__init__(parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    self.ui.Send.clicked.connect(self.send)
    timer = QtCore.QTimer()
    timer.timeout.connect(self.view)
    timer.start(3000)
    self.ui.CreateTalkRoom.clicked.connect(self.createtalkrooms)
    self.ui.TalkRooms.itemClicked.connect(self.onItemClicked)
  def createtalkrooms(self):
    roomname = self.ui.CreateTalkRoomForm.text()
    res = requests.post("http://junkychat.herokuapp.com/create", params={"roomname":roomname}).text
    print(res)
    self.rooms()
  def send(self):
    msg = self.ui.MessageForm.toPlainText()
    print(msg)
    send_date = datetime.now()
    roomname = self.selectedroomname
    print(roomname)
    data = {"msg":"["+str(send_date)+"] "+"["+str(user_name)+":] "+str(msg),"roomname":roomname}
    res = requests.post('https://junkychat.herokuapp.com/send',data=data)
    self.view()
  @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
  def onItemClicked(self, it, col):
    self.selectedroomname = it.text(col)
    print(self.selectedroomname)
    self.view()
  def rooms(self):
    self.roomitems = []
    roomid = 0
    rooms = requests.get("https://junkychat.herokuapp.com/rooms").text#リストでreturn
    rooms = eval(rooms)
    print(rooms)
    print(type(rooms))
    for room in rooms:
      print("room: " + room)
      roomi = QtWidgets.QTreeWidgetItem(self.ui.TalkRooms)
      self.roomitems.append(roomi.setText(roomid, room))
      roomid = roomid + 1
    print(self.roomitems)
    self.ui.roomitem = QtWidgets.QTreeWidgetItem(self.ui.TalkRooms)
    self.ui.roomitem.addChildren(self.roomitems)
  def view(self):
    self.rooms()
    msg_list = []
    ret_msg = ""
    msgs = requests.get("https://junkychat.herokuapp.com/view", params={"selectedroomname":self.selectedroomname}).text
    print(msgs)
    msgs = eval(msgs)
    print(msgs)
    for msg in msgs:
      print(msg)
      ret_msg = ret_msg + "\n" + msg["msg"]
    print(ret_msg)
    self.ui.MessageLogs.setText(ret_msg)
if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Test()
  window.show()
  sys.exit(app.exec_())