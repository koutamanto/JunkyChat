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
    self.view()
  def send(self):
    msg = self.ui.MessageForm.toPlainText()
    print(msg)
    send_date = datetime.now()
    roomname = self.selectedroomname
    data = json.dumps({{"msg":"["+str(send_date)+"] "+"["+user_name+":] "+msg},{"roomname":roomname}})
    res = requests.post('https://junkychat.herokuapp.com/send',data=data)
    self.view()
  @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
  def onItemClicked(self, it, col):
    self.selectedroomname = it.text(col)
    print(self.selectedroomname)
    self.view()
  def view(self):
    roomid = 0
    msg_list = []
    ret_msg = ""
    msgs = requests.get("https://junkychat.herokuapp.com/view", params={"selectedroomname":self.selectedroomname}).text
    msgs = eval(msgs)["datas"]
    print(msgs)
    for msg in msgs:
      print(msg)
      ret_msg = ret_msg + "\n" + msg["msg"]
    print(ret_msg)
    self.ui.MessageLogs.setText(ret_msg)
    rooms = requests.get("https://junkychat.herokuapp.com/rooms",params={"selectedroomname":self.selectedroomname}).text#リストでreturn
    roomitems = QtWidgets.QTreeWidgetItem(self.ui.TalkRooms)
    for room in eval(rooms):
      roomitems.addChild(tr(room))
if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Test()
  window.show()
  sys.exit(app.exec_())