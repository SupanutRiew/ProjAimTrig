import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
import sqlite3
#DONE  
class Firstpage(QDialog):
    def __init__(self):
        super(Firstpage, self).__init__()   #use init of QDialog
        loadUi("Firstpage.ui",self)
        self.gotologinpage.clicked.connect(self.login)
        self.setup.clicked.connect(self.setupchyt)
        self.deletebutton.clicked.connect(self.delete)
    #go to login page
    def login(self):
        login = Loginpage()
        widget.addWidget(login)#currently firstpage is widget A and login page is widget A+1
        widget.setCurrentIndex(widget.currentIndex()+1)#go to login page by set index A+1
    #go to setup page
    def setupchyt(self):
        setup = setuppage()
        widget.addWidget(setup)
        widget.setCurrentIndex(widget.currentIndex()+1)
    #go to delete page
    def delete(self):
        delete = deletepage()
        widget.addWidget(delete)
        widget.setCurrentIndex(widget.currentIndex()+1)
#DONE    
class Loginpage(QDialog):
    def __init__(self):
        super(Loginpage, self).__init__()
        loadUi("Loginpage.ui",self)
        self.gobackfromlogin.clicked.connect(self.goback)
        self.loginbutton.clicked.connect(self.loginfunc)
    #back to first page
    def goback(self):
        back = Firstpage()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)
    #login
    def loginfunc(self):
        global myfuckingid
        global tofindmatch   #this will be used in the matchpage
        global tofindgoal
        proid = self.productid.text()
        password = self.password.text()
        if proid == "" or password == "":
            self.errormessage.setText("Input all fields")
        else:
            connect = sqlite3.connect("account.db")
            cur = connect.cursor()
            query = 'SELECT productpassword FROM login WHERE productID =\''+proid+"\'"
            cur.execute(query)
            try:
                result = cur.fetchone()[0]
                if result == password:
                    newquery = 'SELECT producttag FROM login WHERE productID =\''+proid+"\'"
                    cur.execute(newquery)
                    tofindmatch = cur.fetchone()[0] #later
                    ewquery = 'SELECT goaltag FROM login WHERE productID =\''+proid+"\'"
                    cur.execute(ewquery)
                    tofindgoal = cur.fetchone()[0] #later
                    myfuckingid = proid #later
                    match = matchpage()
                    widget.addWidget(match)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    self.errormessage.setText("Invalid password")
            except:
                self.errormessage.setText("Account does not exist")
class matchpage(QDialog):
    def __init__(self):
        super(matchpage, self).__init__()
        loadUi("matchpage.ui", self)
        self.tableWidget.setColumnWidth(0, 279)
        self.tableWidget.setColumnWidth(1, 279)
        self.tableWidget.setColumnWidth(2, 279)
        self.tableWidget.setColumnWidth(3, 183)
        self.tableWidget.setVisible(False)
        self.returntologin.clicked.connect(self.gologin)
        self.showbutton.clicked.connect(self.display)
    #display on table
    def display(self):
        self.tableWidget.setVisible(True)
        connect = sqlite3.connect("account.db")
        cur = connect.cursor()
        sqlquery = "SELECT * FROM login"
        rowcount = 1
        table =0
        addshit = 0
        for row in cur.execute(sqlquery):#look into each data one at a time
            
            hisid, name, descrip, contact, blobimage, hisgoal, histag =  row[0], row[3], row[4], row[2], row[7], row[6], row[5]
            if myfuckingid != hisid:
                if tofindmatch in hisgoal:
                    if histag in tofindgoal:
                        addshit+= 1
                        if addshit >= 3:
                            self.tableWidget.setColumnWidth(0, 273)#change width size due to additional scroll area
                            self.tableWidget.setColumnWidth(1, 274)
                            self.tableWidget.setColumnWidth(2, 273)
                            self.tableWidget.setColumnWidth(3, 183)
                            
                        self.tableWidget.setRowCount(rowcount)
                        self.tableWidget.setRowHeight(table, 183)
                        #change this shit image
                        self.tableWidget.setItem(table, 0, QtWidgets.QTableWidgetItem(name))
                        self.tableWidget.setItem(table, 1, QtWidgets.QTableWidgetItem(descrip))
                        self.tableWidget.setItem(table, 2, QtWidgets.QTableWidgetItem(contact))
                        #from here to pixmap delete
                        item = self.getImageLabel(blobimage)
                        #convert finished. Now how do i fucking add it to the table
                        self.tableWidget.setCellWidget(table, 3, item)
                        rowcount+=1
                        table+=1
                        
    def getImageLabel(self,blobimage):
        #เป็นเหี้ยอะไรวะไอสัส
        newlabel = QtWidgets.QLabel()#add new label
        newlabel.setText("")
        pixmap = QPixmap()
        pixmap.loadFromData(blobimage)#get image
        puxmap = pixmap.scaled(183,183)
        newlabel.setPixmap(puxmap) #set image to label
        return newlabel
    #back to login
    def gologin(self):
        login = Loginpage()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

class setuppage(QDialog):
    def __init__(self):
        super(setuppage, self).__init__()
        loadUi("setuppage.ui",self)
        setuppage.listgood = []
        self.gobackfromsetup.clicked.connect(self.goback)
        self.mytag.currentIndexChanged.connect(self.realtag)
        self.uploadimagebutton.clicked.connect(self.loadimage)
        self.finishsetupbutton.clicked.connect(self.confirm)
        self.checkallclothes.clicked.connect(self.allclothes)
        self.checkallaccessories.clicked.connect(self.allaccessories)
        self.checkallshoes.clicked.connect(self.allshoes)
        self.checkallmobile.clicked.connect(self.allmobile)
        self.checkallcom.clicked.connect(self.allcom)
        self.checkallbags.clicked.connect(self.allbags)
        self.checkallcameras.clicked.connect(self.allcameras)
        self.checkallgames.clicked.connect(self.allgames)
        self.checkallhomeen.clicked.connect(self.allhomeen)
        self.checkallhomeapp.clicked.connect(self.allhomeapp)
        self.checkallsports.clicked.connect(self.allsports)
        self.uncheckall.clicked.connect(self.uncheck)
        self.checkall.clicked.connect(self.fuckin)
        
        self.pajamas.stateChanged.connect(self.pajamasclothes)
        self.tanktops.stateChanged.connect(self.tanktopsclothes)
        self.sportssweaters.stateChanged.connect(self.sportssweatersclothes)
        self.suitjackets.stateChanged.connect(self.suitjacketsclothes)
        self.leatherjackets.stateChanged.connect(self.leatherjacketsclothes)
        self.overcoats.stateChanged.connect(self.overcoatsclothes)
        self.tshirts.stateChanged.connect(self.tshirtsclothes)
        self.shirts.stateChanged.connect(self.shirtsclothes)
        self.hoodies.stateChanged.connect(self.hoodiesclothes)
        self.sweaters.stateChanged.connect(self.sweatersclothes)
        self.poloshirts.stateChanged.connect(self.poloshirtsclothes)
        self.dresses.stateChanged.connect(self.dressesclothes)
        self.croppedshirts.stateChanged.connect(self.croppedshirtsclothes)
        self.jeans.stateChanged.connect(self.jeansclothes)
        self.workpants.stateChanged.connect(self.workpantsclothes)
        self.shorts.stateChanged.connect(self.shortsclothes)
        self.sportspants.stateChanged.connect(self.sportspantsclothes)
        self.suitpants.stateChanged.connect(self.suitpantsclothes)
        self.skirts.stateChanged.connect(self.skirtsclothes)
        self.sportsshorts.stateChanged.connect(self.sportsshortsclothes)
        self.leggings.stateChanged.connect(self.leggingsclothes)
        self.leatherpants.stateChanged.connect(self.leatherpantsclothes)
        self.fittedsuitpants.stateChanged.connect(self.fittedsuitpantsclothes)
        self.otherclothes.stateChanged.connect(self.otherclothesclothes)
        
        self.chains.stateChanged.connect(self.chainsaccessories)
        self.earrings.stateChanged.connect(self.earringsaccessories)
        self.scarves.stateChanged.connect(self.scarvesaccessories)
        self.ties.stateChanged.connect(self.tiesaccessories)
        self.bangles.stateChanged.connect(self.banglesaccessories)
        self.leatherstraps.stateChanged.connect(self.leatherstrapsaccessories)
        self.necklaces.stateChanged.connect(self.necklacesaccessories)
        self.watches.stateChanged.connect(self.watchesaccessories)
        self.gloves.stateChanged.connect(self.glovesaccessories)
        self.cuffs.stateChanged.connect(self.cuffsaccessories)
        self.suspenders.stateChanged.connect(self.suspendersaccessories)
        self.hats.stateChanged.connect(self.hatsaccessories)
        self.glasses.stateChanged.connect(self.glassesaccessories)
        self.otheraccessories.stateChanged.connect(self.otheraccessoriesaccessories)

        self.boots.stateChanged.connect(self.bootsshoes)
        self.highheelboots.stateChanged.connect(self.highheelbootsshoes)
        self.sneakers.stateChanged.connect(self.sneakersshoes)
        self.skateshoes.stateChanged.connect(self.skateshoesshoes)
        self.flipflops.stateChanged.connect(self.flipflopsshoes) 
        self.runningshoes.stateChanged.connect(self.runningshoesshoes)
        self.sportshoes.stateChanged.connect(self.sportshoesshoes)
        self.smartshoes.stateChanged.connect(self.smartshoesshoes)
        self.sandals.stateChanged.connect(self.sandalsshoes)
        self.slipons.stateChanged.connect(self.sliponsshoes)
        self.othershoes.stateChanged.connect(self.othershoesshoes)

        self.backpackwaistbags.stateChanged.connect(self.backpackwaistbagsbags)
        self.clutchhandheldbags.stateChanged.connect(self.clutchhandheldbagsbags)
        self.crossbodyshoulderbags.stateChanged.connect(self.crossbodyshoulderbagsbags)
        self.athleticbags.stateChanged.connect(self.athleticbagsbags)
        self.luggagetrunks.stateChanged.connect(self.luggagetrunksbags)
        self.walletspurses.stateChanged.connect(self.walletspursesbags)
        self.leathergoods.stateChanged.connect(self.leathergoodsbags)
        self.otherbags.stateChanged.connect(self.otherbagsbags)

        self.earphones.stateChanged.connect(self.earphonesmobile)
        self.cableschargers.stateChanged.connect(self.cableschargersmobile)
        self.powerbank.stateChanged.connect(self.powerbankmobile)
        self.tablet.stateChanged.connect(self.tabletmobile)
        self.casescovers.stateChanged.connect(self.casescoversmobile)
        self.screenprotector.stateChanged.connect(self.screenprotectormobile)
        self.mobilephones.stateChanged.connect(self.mobilephonesmobile)
        self.othermobilegadgets.stateChanged.connect(self.othermobilegadgetsmobile)

        self.laptop.stateChanged.connect(self.laptopcom)
        self.mousekeyboard.stateChanged.connect(self.mousekeyboardcom)
        self.headphones.stateChanged.connect(self.headphonescom)
        self.speakers.stateChanged.connect(self.speakerscom)
        self.microphones.stateChanged.connect(self.microphonescom)
        self.printers.stateChanged.connect(self.printerscom)
        self.monitors.stateChanged.connect(self.monitorscom)
        self.computers.stateChanged.connect(self.computerscom)
        self.cables.stateChanged.connect(self.cablescom)
        self.chargers.stateChanged.connect(self.chargerscom)
        self.othercomputerslaptop.stateChanged.connect(self.othercomputerslaptopcom)

        self.cameras.stateChanged.connect(self.camerascam)
        self.actioncameras.stateChanged.connect(self.actioncamerascam)
        self.film.stateChanged.connect(self.filmcam)
        self.lens.stateChanged.connect(self.lenscam)
        self.cctv.stateChanged.connect(self.cctvcam)
        self.additionalgears.stateChanged.connect(self.additionalgearscam)
        self.othercameras.stateChanged.connect(self.othercamerascam)

        self.discscartridges.stateChanged.connect(self.discscartridgesgames)
        self.gaminggears.stateChanged.connect(self.gaminggearsgames)
        self.collectibles.stateChanged.connect(self.collectiblesgames)
        self.souvenirs.stateChanged.connect(self.souvenirsgames)
        self.boardgames.stateChanged.connect(self.boardgamesgames)
        self.othergames.stateChanged.connect(self.othergamesgames)

        self.tv.stateChanged.connect(self.tvhomeen)
        self.projectors.stateChanged.connect(self.projectorshomeen)
        self.mediaplayers.stateChanged.connect(self.mediaplayershomeen)
        self.musicinstruments.stateChanged.connect(self.musicinstrumentshomeen)
        self.otherhomeentertainment.stateChanged.connect(self.otherhomeentertainmenthomeen)

        self.microwaveoven.stateChanged.connect(self.microwaveovenhomeapp)
        self.fan.stateChanged.connect(self.fanhomeapp)
        self.refrigerator.stateChanged.connect(self.refrigeratorhomeapp)
        self.airconditioner.stateChanged.connect(self.airconditionerhomeapp)
        self.airpurifier.stateChanged.connect(self.airpurifierhomeapp)
        self.vacuumcleaner.stateChanged.connect(self.vacuumcleanerhomeapp)
        self.washingmachine.stateChanged.connect(self.washingmachinehomeapp)
        self.otherhomeappliances.stateChanged.connect(self.otherhomeapplianceshomeapp)

        self.fitness.stateChanged.connect(self.fitnesssports)
        self.campinggears.stateChanged.connect(self.campinggearssports)
        self.fishing.stateChanged.connect(self.fishingsports)
        self.climbinggears.stateChanged.connect(self.climbinggearssports)
        self.skateboards.stateChanged.connect(self.skateboardssports)
        self.scooters.stateChanged.connect(self.scooterssports)
        self.football.stateChanged.connect(self.footballsports)
        self.basketball.stateChanged.connect(self.basketballsports)
        self.tennis.stateChanged.connect(self.tennissports)
        self.badminton.stateChanged.connect(self.badmintonsports)
        self.tabletennis.stateChanged.connect(self.tabletennissports)
        self.baseball.stateChanged.connect(self.baseballsports)
        self.divinggears.stateChanged.connect(self.divinggearssports)
        self.surf.stateChanged.connect(self.surfsports)
        self.bicyclegears.stateChanged.connect(self.bicyclegearssports)
        self.golf.stateChanged.connect(self.golfsports)
        self.rugby.stateChanged.connect(self.rugbysports)
        self.otherbags_2.stateChanged.connect(self.otherbags_2sports)

        self.others.stateChanged.connect(self.otherszzz)
    #finish set up
    def confirm(self):
        samecount = 0
        prodid = self.productid.text()
        passw = self.password.text()
        contact = self.contactinfo.text()
        name = self.productname.text()
        prodtag = self.smalltag.currentText()
        descrip = self.description.toPlainText()
        goal = setuppage.listgood
        # how tf do i add picture
        if prodid == "" or passw == "" or contact == "" or name == "" or descrip == "":
            self.errormessage.setText("Fill Out All Fields")
        elif goal == []:
            self.errormessage.setText("Choose at least one goal")
        else:
            connect = sqlite3.connect("account.db")
            cur = connect.cursor()
            query = 'SELECT productid FROM login'
            cur.execute(query)
            result = cur.fetchall()
            #This prevent multiple products from having same ids.
            for i in range (len(result)):
                if prodid in result[i]:
                    samecount+=1
            if samecount > 0:
                self.errormessage.setText("This Product ID already exists")
            else:
                #use % to separate instead of list
                self.errormessage.setText("")
                goalstring = '%'.join([str(item) for item in goal])
                goalstring = '%' + goalstring + '%'
                prodtag = '%' + prodtag + '%'
          
                try:
                    info = [prodid, passw, contact, name, descrip, prodtag, goalstring, baseimagereal]#add image duay(Global variable from addimage function
                    cur.execute('INSERT INTO login VALUES(?,?,?,?,?,?,?,?)', info)
                    connect.commit()
                    connect.close()
                    back = Firstpage()
                    widget.addWidget(back)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                except:
                    self.errormessage.setText("Add an image")
    #uncheck all
    def uncheck(self):
        self.others.setChecked(False)
        
        self.chains.setChecked(False)
        self.earrings.setChecked(False)
        self.scarves.setChecked(False)
        self.ties.setChecked(False)
        self.bangles.setChecked(False)
        self.leatherstraps.setChecked(False)
        self.necklaces.setChecked(False)
        self.watches.setChecked(False)
        self.gloves.setChecked(False)
        self.cuffs.setChecked(False)
        self.suspenders.setChecked(False)
        self.hats.setChecked(False)
        self.glasses.setChecked(False)
        self.otheraccessories.setChecked(False)

        self.boots.setChecked(False)
        self.highheelboots.setChecked(False)
        self.sneakers.setChecked(False)
        self.skateshoes.setChecked(False)
        self.flipflops.setChecked(False)
        self.runningshoes.setChecked(False)
        self.sportshoes.setChecked(False)
        self.smartshoes.setChecked(False)
        self.sandals.setChecked(False)
        self.slipons.setChecked(False)
        self.othershoes.setChecked(False)

        self.backpackwaistbags.setChecked(False)
        self.clutchhandheldbags.setChecked(False)
        self.crossbodyshoulderbags.setChecked(False)
        self.athleticbags.setChecked(False)
        self.luggagetrunks.setChecked(False)
        self.walletspurses.setChecked(False)
        self.leathergoods.setChecked(False)
        self.otherbags.setChecked(False)

        self.earphones.setChecked(False)
        self.cableschargers.setChecked(False)
        self.powerbank.setChecked(False)
        self.tablet.setChecked(False)
        self.casescovers.setChecked(False)
        self.screenprotector.setChecked(False)
        self.mobilephones.setChecked(False)
        self.othermobilegadgets.setChecked(False)

        self.laptop.setChecked(False)
        self.mousekeyboard.setChecked(False)
        self.headphones.setChecked(False)
        self.speakers.setChecked(False)
        self.microphones.setChecked(False)
        self.printers.setChecked(False)
        self.monitors.setChecked(False)
        self.computers.setChecked(False)
        self.cables.setChecked(False)
        self.chargers.setChecked(False)
        self.othercomputerslaptop.setChecked(False)

        self.cameras.setChecked(False)
        self.actioncameras.setChecked(False)
        self.film.setChecked(False)
        self.lens.setChecked(False)
        self.cctv.setChecked(False)
        self.additionalgears.setChecked(False)
        self.othercameras.setChecked(False)

        self.discscartridges.setChecked(False)
        self.gaminggears.setChecked(False)
        self.collectibles.setChecked(False)
        self.souvenirs.setChecked(False)
        self.boardgames.setChecked(False)
        self.othergames.setChecked(False)

        self.tv.setChecked(False)
        self.projectors.setChecked(False)
        self.mediaplayers.setChecked(False)
        self.musicinstruments.setChecked(False)
        self.otherhomeentertainment.setChecked(False)
        
        self.pajamas.setChecked(False)
        self.tanktops.setChecked(False)
        self.sportssweaters.setChecked(False)
        self.suitjackets.setChecked(False)
        self.leatherjackets.setChecked(False)
        self.overcoats.setChecked(False)
        self.tshirts.setChecked(False)
        self.shirts.setChecked(False)
        self.hoodies.setChecked(False)
        self.sweaters.setChecked(False)
        self.poloshirts.setChecked(False)
        self.dresses.setChecked(False)
        self.croppedshirts.setChecked(False)
        self.jeans.setChecked(False)
        self.workpants.setChecked(False)
        self.shorts.setChecked(False)
        self.sportspants.setChecked(False)
        self.suitpants.setChecked(False)
        self.skirts.setChecked(False)
        self.sportsshorts.setChecked(False)
        self.leggings.setChecked(False)
        self.leatherpants.setChecked(False)
        self.fittedsuitpants.setChecked(False)
        self.otherclothes.setChecked(False)        
        
        self.microwaveoven.setChecked(False)
        self.fan.setChecked(False)
        self.refrigerator.setChecked(False)
        self.airconditioner.setChecked(False)
        self.airpurifier.setChecked(False)
        self.vacuumcleaner.setChecked(False)
        self.washingmachine.setChecked(False)
        self.otherhomeappliances.setChecked(False)

        self.fitness.setChecked(False)
        self.campinggears.setChecked(False)
        self.fishing.setChecked(False)
        self.climbinggears.setChecked(False)
        self.skateboards.setChecked(False)
        self.scooters.setChecked(False)
        self.football.setChecked(False)
        self.basketball.setChecked(False)
        self.tennis.setChecked(False)
        self.badminton.setChecked(False)
        self.tabletennis.setChecked(False)
        self.baseball.setChecked(False)
        self.divinggears.setChecked(False)
        self.surf.setChecked(False)
        self.bicyclegears.setChecked(False)
        self.golf.setChecked(False)
        self.rugby.setChecked(False)
        self.otherbags_2.setChecked(False)
    #check all clothes
    def allclothes(self):
        self.pajamas.setChecked(True)
        self.tanktops.setChecked(True)
        self.sportssweaters.setChecked(True)
        self.suitjackets.setChecked(True)
        self.leatherjackets.setChecked(True)
        self.overcoats.setChecked(True)
        self.tshirts.setChecked(True)
        self.shirts.setChecked(True)
        self.hoodies.setChecked(True)
        self.sweaters.setChecked(True)
        self.poloshirts.setChecked(True)
        self.dresses.setChecked(True)
        self.croppedshirts.setChecked(True)
        self.jeans.setChecked(True)
        self.workpants.setChecked(True)
        self.shorts.setChecked(True)
        self.sportspants.setChecked(True)
        self.suitpants.setChecked(True)
        self.skirts.setChecked(True)
        self.sportsshorts.setChecked(True)
        self.leggings.setChecked(True)
        self.leatherpants.setChecked(True)
        self.fittedsuitpants.setChecked(True)
        self.otherclothes.setChecked(True)
    #check all accessories
    def allaccessories(self):
        self.chains.setChecked(True)
        self.earrings.setChecked(True)
        self.scarves.setChecked(True)
        self.ties.setChecked(True)
        self.bangles.setChecked(True)
        self.leatherstraps.setChecked(True)
        self.necklaces.setChecked(True)
        self.watches.setChecked(True)
        self.gloves.setChecked(True)
        self.cuffs.setChecked(True)
        self.suspenders.setChecked(True)
        self.hats.setChecked(True)
        self.glasses.setChecked(True)
        self.otheraccessories.setChecked(True)
    #check all shoes
    def allshoes(self):
        self.boots.setChecked(True)
        self.highheelboots.setChecked(True)
        self.sneakers.setChecked(True)
        self.skateshoes.setChecked(True)
        self.flipflops.setChecked(True)
        self.runningshoes.setChecked(True)
        self.sportshoes.setChecked(True)
        self.smartshoes.setChecked(True)
        self.sandals.setChecked(True)
        self.slipons.setChecked(True)
        self.othershoes.setChecked(True)
    #check all bags
    def allbags(self):
        self.backpackwaistbags.setChecked(True)
        self.clutchhandheldbags.setChecked(True)
        self.crossbodyshoulderbags.setChecked(True)
        self.athleticbags.setChecked(True)
        self.luggagetrunks.setChecked(True)
        self.walletspurses.setChecked(True)
        self.leathergoods.setChecked(True)
        self.otherbags.setChecked(True)
    #check all mobile
    def allmobile(self):
        self.earphones.setChecked(True)
        self.cableschargers.setChecked(True)
        self.powerbank.setChecked(True)
        self.tablet.setChecked(True)
        self.casescovers.setChecked(True)
        self.screenprotector.setChecked(True)
        self.mobilephones.setChecked(True)
        self.othermobilegadgets.setChecked(True)
    #Check all com
    def allcom(self):
        self.laptop.setChecked(True)
        self.mousekeyboard.setChecked(True)
        self.headphones.setChecked(True)
        self.speakers.setChecked(True)
        self.microphones.setChecked(True)
        self.printers.setChecked(True)
        self.monitors.setChecked(True)
        self.computers.setChecked(True)
        self.cables.setChecked(True)
        self.chargers.setChecked(True)
        self.othercomputerslaptop.setChecked(True)
    #Check all cameras
    def allcameras(self):
        self.cameras.setChecked(True)
        self.actioncameras.setChecked(True)
        self.film.setChecked(True)
        self.lens.setChecked(True)
        self.cctv.setChecked(True)
        self.additionalgears.setChecked(True)
        self.othercameras.setChecked(True)
    #check all games
    def allgames(self):
        self.discscartridges.setChecked(True)
        self.gaminggears.setChecked(True)
        self.collectibles.setChecked(True)
        self.souvenirs.setChecked(True)
        self.boardgames.setChecked(True)
        self.othergames.setChecked(True)
    #check all homeen
    def allhomeen(self):
        self.tv.setChecked(True)
        self.projectors.setChecked(True)
        self.mediaplayers.setChecked(True)
        self.musicinstruments.setChecked(True)
        self.otherhomeentertainment.setChecked(True)
    #check all homeapp
    def allhomeapp(self):
        self.microwaveoven.setChecked(True)
        self.fan.setChecked(True)
        self.refrigerator.setChecked(True)
        self.airconditioner.setChecked(True)
        self.airpurifier.setChecked(True)
        self.vacuumcleaner.setChecked(True)
        self.washingmachine.setChecked(True)
        self.otherhomeappliances.setChecked(True)
    #check  all sports
    def allsports(self):
        self.fitness.setChecked(True)
        self.campinggears.setChecked(True)
        self.fishing.setChecked(True)
        self.climbinggears.setChecked(True)
        self.skateboards.setChecked(True)
        self.scooters.setChecked(True)
        self.football.setChecked(True)
        self.basketball.setChecked(True)
        self.tennis.setChecked(True)
        self.badminton.setChecked(True)
        self.tabletennis.setChecked(True)
        self.baseball.setChecked(True)
        self.divinggears.setChecked(True)
        self.surf.setChecked(True)
        self.bicyclegears.setChecked(True)
        self.golf.setChecked(True)
        self.rugby.setChecked(True)
        self.otherbags_2.setChecked(True)
    #check all
    def fuckin(self):
        self.others.setChecked(True)
        
        self.chains.setChecked(True)
        self.earrings.setChecked(True)
        self.scarves.setChecked(True)
        self.ties.setChecked(True)
        self.bangles.setChecked(True)
        self.leatherstraps.setChecked(True)
        self.necklaces.setChecked(True)
        self.watches.setChecked(True)
        self.gloves.setChecked(True)
        self.cuffs.setChecked(True)
        self.suspenders.setChecked(True)
        self.hats.setChecked(True)
        self.glasses.setChecked(True)
        self.otheraccessories.setChecked(True)

        self.boots.setChecked(True)
        self.highheelboots.setChecked(True)
        self.sneakers.setChecked(True)
        self.skateshoes.setChecked(True)
        self.flipflops.setChecked(True)
        self.runningshoes.setChecked(True)
        self.sportshoes.setChecked(True)
        self.smartshoes.setChecked(True)
        self.sandals.setChecked(True)
        self.slipons.setChecked(True)
        self.othershoes.setChecked(True)

        self.backpackwaistbags.setChecked(True)
        self.clutchhandheldbags.setChecked(True)
        self.crossbodyshoulderbags.setChecked(True)
        self.athleticbags.setChecked(True)
        self.luggagetrunks.setChecked(True)
        self.walletspurses.setChecked(True)
        self.leathergoods.setChecked(True)
        self.otherbags.setChecked(True)

        self.earphones.setChecked(True)
        self.cableschargers.setChecked(True)
        self.powerbank.setChecked(True)
        self.tablet.setChecked(True)
        self.casescovers.setChecked(True)
        self.screenprotector.setChecked(True)
        self.mobilephones.setChecked(True)
        self.othermobilegadgets.setChecked(True)

        self.laptop.setChecked(True)
        self.mousekeyboard.setChecked(True)
        self.headphones.setChecked(True)
        self.speakers.setChecked(True)
        self.microphones.setChecked(True)
        self.printers.setChecked(True)
        self.monitors.setChecked(True)
        self.computers.setChecked(True)
        self.cables.setChecked(True)
        self.chargers.setChecked(True)
        self.othercomputerslaptop.setChecked(True)

        self.cameras.setChecked(True)
        self.actioncameras.setChecked(True)
        self.film.setChecked(True)
        self.lens.setChecked(True)
        self.cctv.setChecked(True)
        self.additionalgears.setChecked(True)
        self.othercameras.setChecked(True)

        self.discscartridges.setChecked(True)
        self.gaminggears.setChecked(True)
        self.collectibles.setChecked(True)
        self.souvenirs.setChecked(True)
        self.boardgames.setChecked(True)
        self.othergames.setChecked(True)

        self.tv.setChecked(True)
        self.projectors.setChecked(True)
        self.mediaplayers.setChecked(True)
        self.musicinstruments.setChecked(True)
        self.otherhomeentertainment.setChecked(True)
        
        self.pajamas.setChecked(True)
        self.tanktops.setChecked(True)
        self.sportssweaters.setChecked(True)
        self.suitjackets.setChecked(True)
        self.leatherjackets.setChecked(True)
        self.overcoats.setChecked(True)
        self.tshirts.setChecked(True)
        self.shirts.setChecked(True)
        self.hoodies.setChecked(True)
        self.sweaters.setChecked(True)
        self.poloshirts.setChecked(True)
        self.dresses.setChecked(True)
        self.croppedshirts.setChecked(True)
        self.jeans.setChecked(True)
        self.workpants.setChecked(True)
        self.shorts.setChecked(True)
        self.sportspants.setChecked(True)
        self.suitpants.setChecked(True)
        self.skirts.setChecked(True)
        self.sportsshorts.setChecked(True)
        self.leggings.setChecked(True)
        self.leatherpants.setChecked(True)
        self.fittedsuitpants.setChecked(True)
        self.otherclothes.setChecked(True)        
        
        self.microwaveoven.setChecked(True)
        self.fan.setChecked(True)
        self.refrigerator.setChecked(True)
        self.airconditioner.setChecked(True)
        self.airpurifier.setChecked(True)
        self.vacuumcleaner.setChecked(True)
        self.washingmachine.setChecked(True)
        self.otherhomeappliances.setChecked(True)

        self.fitness.setChecked(True)
        self.campinggears.setChecked(True)
        self.fishing.setChecked(True)
        self.climbinggears.setChecked(True)
        self.skateboards.setChecked(True)
        self.scooters.setChecked(True)
        self.football.setChecked(True)
        self.basketball.setChecked(True)
        self.tennis.setChecked(True)
        self.badminton.setChecked(True)
        self.tabletennis.setChecked(True)
        self.baseball.setChecked(True)
        self.divinggears.setChecked(True)
        self.surf.setChecked(True)
        self.bicyclegears.setChecked(True)
        self.golf.setChecked(True)
        self.rugby.setChecked(True)
        self.otherbags_2.setChecked(True)

#All checkbox starts here____________________________________________________________________________
        
    #check box pajamas
    def pajamasclothes(self):
        if self.pajamas.isChecked() == True:
            setuppage.listgood.append("Pajamas")
            print(setuppage.listgood)
        else:
            if "Pajamas" in setuppage.listgood:
                setuppage.listgood.remove("Pajamas")
                print(setuppage.listgood)
    #check box tank tops
    def tanktopsclothes(self):
        if self.tanktops.isChecked() == True:
            setuppage.listgood.append("Tank Tops")
            print(setuppage.listgood)
        else:
            if "Tank Tops" in setuppage.listgood:
                setuppage.listgood.remove("Tank Tops")
                print(setuppage.listgood)
    #check box sports sweaters
    def sportssweatersclothes(self):
        if self.sportssweaters.isChecked() == True:
            setuppage.listgood.append("Sports Sweaters")
            print(setuppage.listgood)
        else:
            if "Sports Sweaters" in setuppage.listgood:
                setuppage.listgood.remove("Sports Sweaters")
                print(setuppage.listgood)
    # check box suit jackets
    def suitjacketsclothes(self):
        if self.suitjackets.isChecked() == True:
            setuppage.listgood.append("Suit Jackets")
            print(setuppage.listgood)
        else:
            if "Suit Jackets" in setuppage.listgood:
                setuppage.listgood.remove("Suit Jackets")
                print(setuppage.listgood)
    #check box leather jackets
    def leatherjacketsclothes(self):
        if self.leatherjackets.isChecked() == True:
            setuppage.listgood.append("Leather Jackets")
            print(setuppage.listgood)
        else:
            if "Leather Jackets" in setuppage.listgood:
                setuppage.listgood.remove("Leather Jackets")
                print(setuppage.listgood)
    #check box overcoats
    def overcoatsclothes(self):
        if self.overcoats.isChecked() == True:
            setuppage.listgood.append("Overcoats")
            print(setuppage.listgood)
        else:
            if "Overcoats" in setuppage.listgood:
                setuppage.listgood.remove("Overcoats")
                print(setuppage.listgood)
    #check box tshirts
    def tshirtsclothes(self):
        if self.tshirts.isChecked() == True:
            setuppage.listgood.append("T-Shirts")
            print(setuppage.listgood)
        else:
            if "T-Shirts" in setuppage.listgood:
                setuppage.listgood.remove("T-Shirts")
                print(setuppage.listgood)
    #check box shirts
    def shirtsclothes(self):
        if self.shirts.isChecked() == True:
            setuppage.listgood.append("Shirts")
            print(setuppage.listgood)
        else:
            if "Shirts" in setuppage.listgood:
                setuppage.listgood.remove("Shirts")
                print(setuppage.listgood)
    #check box hoodies
    def hoodiesclothes(self):
        if self.hoodies.isChecked() == True:
            setuppage.listgood.append("Hoodies")
            print(setuppage.listgood)
        else:
            if "Hoodies" in setuppage.listgood:
                setuppage.listgood.remove("Hoodies")
                print(setuppage.listgood)
    #check box sweaters
    def sweatersclothes(self):
        if self.sweaters.isChecked() == True:
            setuppage.listgood.append("Sweaters")
            print(setuppage.listgood)
        else:
            if "Sweaters" in setuppage.listgood:
                setuppage.listgood.remove("Sweaters")
                print(setuppage.listgood)
#check box poloshirts
    def poloshirtsclothes(self):
        if self.poloshirts.isChecked() == True:
            setuppage.listgood.append("Polo Shirts")
            print(setuppage.listgood)
        else:
            if "Polo Shirts" in setuppage.listgood:
                setuppage.listgood.remove("Polo Shirts")
                print(setuppage.listgood)
#check box dress
    def dressesclothes(self):
        if self.dresses.isChecked() == True:
            setuppage.listgood.append("Dresses")
            print(setuppage.listgood)
        else:
            if "Dresses" in setuppage.listgood:
                setuppage.listgood.remove("Dresses")
                print(setuppage.listgood)
#check box croppped shirts
    def croppedshirtsclothes(self):
        if self.croppedshirts.isChecked() == True:
            setuppage.listgood.append("Cropped Shirts")
            print(setuppage.listgood)
        else:
            if "Cropped Shirts" in setuppage.listgood:
                setuppage.listgood.remove("Cropped Shirts")
                print(setuppage.listgood)
#check box jeans
    def jeansclothes(self):
        if self.jeans.isChecked() == True:
            setuppage.listgood.append("Jeans")
            print(setuppage.listgood)
        else:
            if "Jeans" in setuppage.listgood:
                setuppage.listgood.remove("Jeans")
                print(setuppage.listgood)
#check box workpants
    def workpantsclothes(self):
        if self.workpants.isChecked() == True:
            setuppage.listgood.append("Work Pants")
            print(setuppage.listgood)
        else:
            if "Work Pants" in setuppage.listgood:
                setuppage.listgood.remove("Work Pants")
                print(setuppage.listgood)
#check box shorts
    def shortsclothes(self):
        if self.shorts.isChecked() == True:
            setuppage.listgood.append("Shorts")
            print(setuppage.listgood)
        else:
            if "Shorts" in setuppage.listgood:
                setuppage.listgood.remove("Shorts")
                print(setuppage.listgood)
#check box sportspants
    def sportspantsclothes(self):
        if self.sportspants.isChecked() == True:
            setuppage.listgood.append("Sports Pants")
            print(setuppage.listgood)
        else:
            if "Sports Pants" in setuppage.listgood:
                setuppage.listgood.remove("Sports Pants")
                print(setuppage.listgood)
#check box suitpants
    def suitpantsclothes(self):
        if self.suitpants.isChecked() == True:
            setuppage.listgood.append("Suit Pants")
            print(setuppage.listgood)
        else:
            if "Suit Pants" in setuppage.listgood:
                setuppage.listgood.remove("Suit Pants")
                print(setuppage.listgood)
#check box skirts
    def skirtsclothes(self):
        if self.skirts.isChecked() == True:
            setuppage.listgood.append("Skirts")
            print(setuppage.listgood)
        else:
            if "Skirts" in setuppage.listgood:
                setuppage.listgood.remove("Skirts")
                print(setuppage.listgood)
#check box sportsshorts
    def sportsshortsclothes(self):
        if self.sportsshorts.isChecked() == True:
            setuppage.listgood.append("Sports Shorts")
            print(setuppage.listgood)
        else:
            if "Sports Shorts" in setuppage.listgood:
                setuppage.listgood.remove("Sports Shorts")
                print(setuppage.listgood)
#check box leggings
    def leggingsclothes(self):
        if self.leggings.isChecked() == True:
            setuppage.listgood.append("Leggings")
            print(setuppage.listgood)
        else:
            if "Leggings" in setuppage.listgood:
                setuppage.listgood.remove("Leggings")
                print(setuppage.listgood)
#check box leatherpants
    def leatherpantsclothes(self):
        if self.leatherpants.isChecked() == True:
            setuppage.listgood.append("Leather Pants")
            print(setuppage.listgood)
        else:
            if "Leather Pants" in setuppage.listgood:
                setuppage.listgood.remove("Leather Pants")
                print(setuppage.listgood)
#check box fittedsuitpants
    def fittedsuitpantsclothes(self):
        if self.fittedsuitpants.isChecked() == True:
            setuppage.listgood.append("Fitted Suit Pants")
            print(setuppage.listgood)
        else:
            if "Fitted Suit Pants" in setuppage.listgood:
                setuppage.listgood.remove("Fitted Suit Pants")
                print(setuppage.listgood)
#check box otherclothes
    def otherclothesclothes(self):
        if self.otherclothes.isChecked() == True:
            setuppage.listgood.append("Other Clothes")
            print(setuppage.listgood)
        else:
            if "Other Clothes" in setuppage.listgood:
                setuppage.listgood.remove("Other Clothes")
                print(setuppage.listgood)

################## The end of Clothes section ###########################

#check box chains
    def chainsaccessories(self):
        if self.chains.isChecked() == True:
            setuppage.listgood.append("Chains")
            print(setuppage.listgood)
        else:
            if "Chains" in setuppage.listgood:
                setuppage.listgood.remove("Chains")
                print(setuppage.listgood)
#check box earrings
    def earringsaccessories(self):
        if self.earrings.isChecked() == True:
            setuppage.listgood.append("Earrings")
            print(setuppage.listgood)
        else:
            if "Earrings" in setuppage.listgood:
                setuppage.listgood.remove("Earrings")
                print(setuppage.listgood)
#check box scarves
    def scarvesaccessories(self):
        if self.scarves.isChecked() == True:
            setuppage.listgood.append("Scarves")
            print(setuppage.listgood)
        else:
            if "Scarves" in setuppage.listgood:
                setuppage.listgood.remove("Scarves")
                print(setuppage.listgood)
#check box ties
    def tiesaccessories(self):
        if self.ties.isChecked() == True:
            setuppage.listgood.append("Ties")
            print(setuppage.listgood)
        else:
            if "Ties" in setuppage.listgood:
                setuppage.listgood.remove("Ties")
                print(setuppage.listgood)
#check box bangles
    def banglesaccessories(self):
        if self.bangles.isChecked() == True:
            setuppage.listgood.append("Bangles")
            print(setuppage.listgood)
        else:
            if "Bangles" in setuppage.listgood:
                setuppage.listgood.remove("Bangles")
                print(setuppage.listgood)
#check box leatherstraps
    def leatherstrapsaccessories(self):
        if self.leatherstraps.isChecked() == True:
            setuppage.listgood.append("Leather Straps")
            print(setuppage.listgood)
        else:
            if "Leather Straps" in setuppage.listgood:
                setuppage.listgood.remove("Leather Straps")
                print(setuppage.listgood)
#check box necklaces
    def necklacesaccessories(self):
        if self.necklaces.isChecked() == True:
            setuppage.listgood.append("Necklaces")
            print(setuppage.listgood)
        else:
            if "Necklaces" in setuppage.listgood:
                setuppage.listgood.remove("Necklaces")
                print(setuppage.listgood)
#check box watches
    def watchesaccessories(self):
        if self.watches.isChecked() == True:
            setuppage.listgood.append("Watches")
            print(setuppage.listgood)
        else:
            if "Watches" in setuppage.listgood:
                setuppage.listgood.remove("Watches")
                print(setuppage.listgood)
#check box gloves
    def glovesaccessories(self):
        if self.gloves.isChecked() == True:
            setuppage.listgood.append("Gloves")
            print(setuppage.listgood)
        else:
            if "Gloves" in setuppage.listgood:
                setuppage.listgood.remove("Gloves")
                print(setuppage.listgood)
#check box cuffs
    def cuffsaccessories(self):
        if self.cuffs.isChecked() == True:
            setuppage.listgood.append("Cuffs")
            print(setuppage.listgood)
        else:
            if "Cuffs" in setuppage.listgood:
                setuppage.listgood.remove("Cuffs")
                print(setuppage.listgood)
#check box suspenders
    def suspendersaccessories(self):
        if self.suspenders.isChecked() == True:
            setuppage.listgood.append("Suspenders")
            print(setuppage.listgood)
        else:
            if "Suspenders" in setuppage.listgood:
                setuppage.listgood.remove("Suspenders")
                print(setuppage.listgood)
#check box hats
    def hatsaccessories(self):
        if self.hats.isChecked() == True:
            setuppage.listgood.append("Hats")
            print(setuppage.listgood)
        else:
            if "Hats" in setuppage.listgood:
                setuppage.listgood.remove("Hats")
                print(setuppage.listgood)

#check box glasses
    def glassesaccessories(self):
        if self.glasses.isChecked() == True:
            setuppage.listgood.append("Glasses")
            print(setuppage.listgood)
        else:
            if "Glasses" in setuppage.listgood:
                setuppage.listgood.remove("Glasses")
                print(setuppage.listgood)

#check box otheraccessories
    def otheraccessoriesaccessories(self):
        if self.otheraccessories.isChecked() == True:
            setuppage.listgood.append("Other Accessories")
            print(setuppage.listgood)
        else:
            if "Other Accessories" in setuppage.listgood:
                setuppage.listgood.remove("Other Accessories")
                print(setuppage.listgood)

################## The end of Accessories section ###########################

#check box boots
    def bootsshoes(self):
        if self.boots.isChecked() == True:
            setuppage.listgood.append("Boots")
            print(setuppage.listgood)
        else:
            if "Boots" in setuppage.listgood:
                setuppage.listgood.remove("Boots")
                print(setuppage.listgood)
#check box highheelboots
    def highheelbootsshoes(self):
        if self.highheelboots.isChecked() == True:
            setuppage.listgood.append("High Heel Boots")
            print(setuppage.listgood)
        else:
            if "High Heel Boots" in setuppage.listgood:
                setuppage.listgood.remove("High Heel Boots")
                print(setuppage.listgood)
#check box sneakers
    def sneakersshoes(self):
        if self.sneakers.isChecked() == True:
            setuppage.listgood.append("Sneakers")
            print(setuppage.listgood)
        else:
            if "Sneakers" in setuppage.listgood:
                setuppage.listgood.remove("Sneakers")
                print(setuppage.listgood)
#check box skateshoes
    def skateshoesshoes(self):
        if self.skateshoes.isChecked() == True:
            setuppage.listgood.append("Skate Shoes")
            print(setuppage.listgood)
        else:
            if "Skate Shoes" in setuppage.listgood:
                setuppage.listgood.remove("Skate Shoes")
                print(setuppage.listgood)
#check box flipflops
    def flipflopsshoes(self):
        if self.flipflops.isChecked() == True:
            setuppage.listgood.append("Flip-Flops")
            print(setuppage.listgood)
        else:
            if "Flip-Flops" in setuppage.listgood:
                setuppage.listgood.remove("Flip-Flops")
                print(setuppage.listgood)
#check box runningshoes
    def runningshoesshoes(self):
        if self.runningshoes.isChecked() == True:
            setuppage.listgood.append("Running Shoes")
            print(setuppage.listgood)
        else:
            if "Running Shoes" in setuppage.listgood:
                setuppage.listgood.remove("Running Shoes")
                print(setuppage.listgood)
#check box sportshoes
    def sportshoesshoes(self):
        if self.sportshoes.isChecked() == True:
            setuppage.listgood.append("Sport Shoes")
            print(setuppage.listgood)
        else:
            if "Sport Shoes" in setuppage.listgood:
                setuppage.listgood.remove("Sport Shoes")
                print(setuppage.listgood)
#check box smartshoes
    def smartshoesshoes(self):
        if self.smartshoes.isChecked() == True:
            setuppage.listgood.append("Smart Shoes")
            print(setuppage.listgood)
        else:
            if "Smart Shoes" in setuppage.listgood:
                setuppage.listgood.remove("Smart Shoes")
                print(setuppage.listgood)
#check box sandals
    def sandalsshoes(self):
        if self.sandals.isChecked() == True:
            setuppage.listgood.append("Sandals")
            print(setuppage.listgood)
        else:
            if "Sandals" in setuppage.listgood:
                setuppage.listgood.remove("Sandals")
                print(setuppage.listgood)
#check box slipons
    def sliponsshoes(self):
        if self.slipons.isChecked() == True:
            setuppage.listgood.append("Slip-Ons")
            print(setuppage.listgood)
        else:
            if "Slip-Ons" in setuppage.listgood:
                setuppage.listgood.remove("Slip-Ons")
                print(setuppage.listgood)
#check box othershoes
    def othershoesshoes(self):
        if self.othershoes.isChecked() == True:
            setuppage.listgood.append("Other Shoes")
            print(setuppage.listgood)
        else:
            if "Other Shoes" in setuppage.listgood:
                setuppage.listgood.remove("Other Shoes")
                print(setuppage.listgood)

################## The end of Shoes section ###########################

#check box backpackwaistbags
    def backpackwaistbagsbags(self):
        if self.backpackwaistbags.isChecked() == True:
            setuppage.listgood.append("Backpack&Waist Bags")
            print(setuppage.listgood)
        else:
            if "Backpack&Waist Bags" in setuppage.listgood:
                setuppage.listgood.remove("Backpack&Waist Bags")
                print(setuppage.listgood)
#check box clutchhandheldbags
    def clutchhandheldbagsbags(self):
        if self.clutchhandheldbags.isChecked() == True:
            setuppage.listgood.append("Clutch&Handheld Bags")
            print(setuppage.listgood)
        else:
            if "Clutch&Handheld Bags" in setuppage.listgood:
                setuppage.listgood.remove("Clutch&Handheld Bags")
                print(setuppage.listgood)
#check box crossbodyshoulderbags
    def crossbodyshoulderbagsbags(self):
        if self.crossbodyshoulderbags.isChecked() == True:
            setuppage.listgood.append("Crossbody&Shoulder Bags")
            print(setuppage.listgood)
        else:
            if "Crossbody&Shoulder Bags" in setuppage.listgood:
                setuppage.listgood.remove("Crossbody&Shoulder Bags")
                print(setuppage.listgood)
#check box athleticbags
    def athleticbagsbags(self):
        if self.athleticbags.isChecked() == True:
            setuppage.listgood.append("Athletic Bags")
            print(setuppage.listgood)
        else:
            if "Athletic Bags" in setuppage.listgood:
                setuppage.listgood.remove("Athletic Bags")
                print(setuppage.listgood)
#check box luggagetrunks
    def luggagetrunksbags(self):
        if self.luggagetrunks.isChecked() == True:
            setuppage.listgood.append("Luggage&Trunks")
            print(setuppage.listgood)
        else:
            if "Luggage&Trunks" in setuppage.listgood:
                setuppage.listgood.remove("Luggage&Trunks")
                print(setuppage.listgood)
#check box walletspurses
    def walletspursesbags(self):
        if self.walletspurses.isChecked() == True:
            setuppage.listgood.append("Wallets&Purses")
            print(setuppage.listgood)
        else:
            if "Wallets&Purses" in setuppage.listgood:
                setuppage.listgood.remove("Wallets&Purses")
                print(setuppage.listgood)
#check box leathergoods
    def leathergoodsbags(self):
        if self.leathergoods.isChecked() == True:
            setuppage.listgood.append("Leather Goods")
            print(setuppage.listgood)
        else:
            if "Leather Goods" in setuppage.listgood:
                setuppage.listgood.remove("Leather Goods")
                print(setuppage.listgood)
#check box otherbags
    def otherbagsbags(self):
        if self.otherbags.isChecked() == True:
            setuppage.listgood.append("Other Bags")
            print(setuppage.listgood)
        else:
            if "Other Bags" in setuppage.listgood:
                setuppage.listgood.remove("Other Bags")
                print(setuppage.listgood)

################## The end of Bags section ###########################

#check box earphones
    def earphonesmobile(self):
        if self.earphones.isChecked() == True:
            setuppage.listgood.append("Earphones")
            print(setuppage.listgood)
        else:
            if "Earphones" in setuppage.listgood:
                setuppage.listgood.remove("Earphones")
                print(setuppage.listgood)
#check box cableschargers
    def cableschargersmobile(self):
        if self.cableschargers.isChecked() == True:
            setuppage.listgood.append("Cables&Chargers")
            print(setuppage.listgood)
        else:
            if "Cables&Chargers" in setuppage.listgood:
                setuppage.listgood.remove("Cables&Chargers")
                print(setuppage.listgood)
#check box powerbank
    def powerbankmobile(self):
        if self.powerbank.isChecked() == True:
            setuppage.listgood.append("Powerbank")
            print(setuppage.listgood)
        else:
            if "Powerbank" in setuppage.listgood:
                setuppage.listgood.remove("Powerbank")
                print(setuppage.listgood)
#check box tablet
    def tabletmobile(self):
        if self.tablet.isChecked() == True:
            setuppage.listgood.append("Tablet")
            print(setuppage.listgood)
        else:
            if "Tablet" in setuppage.listgood:
                setuppage.listgood.remove("Tablet")
                print(setuppage.listgood)
#check box casescovers
    def casescoversmobile(self):
        if self.casescovers.isChecked() == True:
            setuppage.listgood.append("Cases&Covers")
            print(setuppage.listgood)
        else:
            if "Cases&Covers" in setuppage.listgood:
                setuppage.listgood.remove("Cases&Covers")
                print(setuppage.listgood)
#check box screenprotector
    def screenprotectormobile(self):
        if self.screenprotector.isChecked() == True:
            setuppage.listgood.append("Screen Protector")
            print(setuppage.listgood)
        else:
            if "Screen Protector" in setuppage.listgood:
                setuppage.listgood.remove("Screen Protector")
                print(setuppage.listgood)
#check box mobilephones
    def mobilephonesmobile(self):
        if self.mobilephones.isChecked() == True:
            setuppage.listgood.append("Mobile Phones")
            print(setuppage.listgood)
        else:
            if "Mobile Phones" in setuppage.listgood:
                setuppage.listgood.remove("Mobile Phones")
                print(setuppage.listgood)
#check box othermobilegadgets
    def othermobilegadgetsmobile(self):
        if self.othermobilegadgets.isChecked() == True:
            setuppage.listgood.append("Other Mobile Gadgets")
            print(setuppage.listgood)
        else:
            if "Other Mobile Gadgets" in setuppage.listgood:
                setuppage.listgood.remove("Other Mobile Gadgets")
                print(setuppage.listgood)

################## The end of Mobile Gadgets section ###########################

#check box laptop
    def laptopcom(self):
        if self.laptop.isChecked() == True:
            setuppage.listgood.append("Laptop")
            print(setuppage.listgood)
        else:
            if "Laptop" in setuppage.listgood:
                setuppage.listgood.remove("Laptop")
                print(setuppage.listgood)
#check box mousekeyboard
    def mousekeyboardcom(self):
        if self.mousekeyboard.isChecked() == True:
            setuppage.listgood.append("Mouse&Keyboard")
            print(setuppage.listgood)
        else:
            if "Mouse&Keyboard" in setuppage.listgood:
                setuppage.listgood.remove("Mouse&Keyboard")
                print(setuppage.listgood)
#check box headphones
    def headphonescom(self):
        if self.headphones.isChecked() == True:
            setuppage.listgood.append("Headphones")
            print(setuppage.listgood)
        else:
            if "Headphones" in setuppage.listgood:
                setuppage.listgood.remove("Headphones")
                print(setuppage.listgood)
#check box speakers
    def speakerscom(self):
        if self.speakers.isChecked() == True:
            setuppage.listgood.append("Speakers")
            print(setuppage.listgood)
        else:
            if "Speakers" in setuppage.listgood:
                setuppage.listgood.remove("Speakers")
                print(setuppage.listgood)
#check box microphones
    def microphonescom(self):
        if self.microphones.isChecked() == True:
            setuppage.listgood.append("Microphones")
            print(setuppage.listgood)
        else:
            if "Microphones" in setuppage.listgood:
                setuppage.listgood.remove("Microphones")
                print(setuppage.listgood)
#check box printers
    def printerscom(self):
        if self.printers.isChecked() == True:
            setuppage.listgood.append("Printers")
            print(setuppage.listgood)
        else:
            if "Printers" in setuppage.listgood:
                setuppage.listgood.remove("Printers")
                print(setuppage.listgood)
#check box monitors
    def monitorscom(self):
        if self.monitors.isChecked() == True:
            setuppage.listgood.append("Monitors")
            print(setuppage.listgood)
        else:
            if "Monitors" in setuppage.listgood:
                setuppage.listgood.remove("Monitors")
                print(setuppage.listgood)
#check box computers
    def computerscom(self):
        if self.computers.isChecked() == True:
            setuppage.listgood.append("Computers")
            print(setuppage.listgood)
        else:
            if "Computers" in setuppage.listgood:
                setuppage.listgood.remove("Computers")
                print(setuppage.listgood)
#check box cables
    def cablescom(self):
        if self.cables.isChecked() == True:
            setuppage.listgood.append("Cables")
            print(setuppage.listgood)
        else:
            if "Cables" in setuppage.listgood:
                setuppage.listgood.remove("Cables")
                print(setuppage.listgood)
#check box chargers
    def chargerscom(self):
        if self.chargers.isChecked() == True:
            setuppage.listgood.append("Chargers")
            print(setuppage.listgood)
        else:
            if "Chargers" in setuppage.listgood:
                setuppage.listgood.remove("Chargers")
                print(setuppage.listgood)
#check box othercomputerslaptop
    def othercomputerslaptopcom(self):
        if self.othercomputerslaptop.isChecked() == True:
            setuppage.listgood.append("Other Computers&Laptop")
            print(setuppage.listgood)
        else:
            if "Other Computers&Laptop" in setuppage.listgood:
                setuppage.listgood.remove("Other Computers&Laptop")
                print(setuppage.listgood)

################## The end of Computers&Laptop section ###########################

#check box cameras
    def camerascam(self):
        if self.cameras.isChecked() == True:
            setuppage.listgood.append("Cameras")
            print(setuppage.listgood)
        else:
            if "Cameras" in setuppage.listgood:
                setuppage.listgood.remove("Cameras")
                print(setuppage.listgood)
#check box actioncameras
    def actioncamerascam(self):
        if self.actioncameras.isChecked() == True:
            setuppage.listgood.append("Action Cameras")
            print(setuppage.listgood)
        else:
            if "Action Cameras" in setuppage.listgood:
                setuppage.listgood.remove("Action Cameras")
                print(setuppage.listgood)
#check box film
    def filmcam(self):
        if self.film.isChecked() == True:
            setuppage.listgood.append("Film")
            print(setuppage.listgood)
        else:
            if "Film" in setuppage.listgood:
                setuppage.listgood.remove("Film")
                print(setuppage.listgood)
#check box lens
    def lenscam(self):
        if self.lens.isChecked() == True:
            setuppage.listgood.append("Lens")
            print(setuppage.listgood)
        else:
            if "Lens" in setuppage.listgood:
                setuppage.listgood.remove("Lens")
                print(setuppage.listgood)
#check box cctv
    def cctvcam(self):
        if self.cctv.isChecked() == True:
            setuppage.listgood.append("CCTV")
            print(setuppage.listgood)
        else:
            if "CCTV" in setuppage.listgood:
                setuppage.listgood.remove("CCTV")
                print(setuppage.listgood)
#check box additionalgears
    def additionalgearscam(self):
        if self.additionalgears.isChecked() == True:
            setuppage.listgood.append("Additional Gears")
            print(setuppage.listgood)
        else:
            if "Additional Gears" in setuppage.listgood:
                setuppage.listgood.remove("Additional Gears")
                print(setuppage.listgood)
#check box othercameras
    def othercamerascam(self):
        if self.othercameras.isChecked() == True:
            setuppage.listgood.append("Other Cameras")
            print(setuppage.listgood)
        else:
            if "Other Cameras" in setuppage.listgood:
                setuppage.listgood.remove("Other Cameras")
                print(setuppage.listgood)

################## The end of Cameras section ###########################

#check box discscartridges
    def discscartridgesgames(self):
        if self.discscartridges.isChecked() == True:
            setuppage.listgood.append("Discs&Cartridges")
            print(setuppage.listgood)
        else:
            if "Discs&Cartridges" in setuppage.listgood:
                setuppage.listgood.remove("Discs&Cartridges")
                print(setuppage.listgood)
#check box gaminggears
    def gaminggearsgames(self):
        if self.gaminggears.isChecked() == True:
            setuppage.listgood.append("Gaming Gears")
            print(setuppage.listgood)
        else:
            if "Gaming Gears" in setuppage.listgood:
                setuppage.listgood.remove("Gaming Gears")
                print(setuppage.listgood)
#check box collectibles
    def collectiblesgames(self):
        if self.collectibles.isChecked() == True:
            setuppage.listgood.append("Collectibles")
            print(setuppage.listgood)
        else:
            if "Collectibles" in setuppage.listgood:
                setuppage.listgood.remove("Collectibles")
                print(setuppage.listgood)
#check box souvenirs
    def souvenirsgames(self):
        if self.souvenirs.isChecked() == True:
            setuppage.listgood.append("Souvenirs")
            print(setuppage.listgood)
        else:
            if "Souvenirs" in setuppage.listgood:
                setuppage.listgood.remove("Souvenirs")
                print(setuppage.listgood)
#check box boardgames
    def boardgamesgames(self):
        if self.boardgames.isChecked() == True:
            setuppage.listgood.append("Board Games")
            print(setuppage.listgood)
        else:
            if "Board Games" in setuppage.listgood:
                setuppage.listgood.remove("Board Games")
                print(setuppage.listgood)
#check box othergames
    def othergamesgames(self):
        if self.othergames.isChecked() == True:
            setuppage.listgood.append("Other Games")
            print(setuppage.listgood)
        else:
            if "Other Games" in setuppage.listgood:
                setuppage.listgood.remove("Other Games")
                print(setuppage.listgood)

################## The end of Games section ###########################

#check box tv
    def tvhomeen(self):
        if self.tv.isChecked() == True:
            setuppage.listgood.append("TV")
            print(setuppage.listgood)
        else:
            if "TV" in setuppage.listgood:
                setuppage.listgood.remove("TV")
                print(setuppage.listgood)
#check box projectors
    def projectorshomeen(self):
        if self.projectors.isChecked() == True:
            setuppage.listgood.append("Projectors")
            print(setuppage.listgood)
        else:
            if "Projectors" in setuppage.listgood:
                setuppage.listgood.remove("Projectors")
                print(setuppage.listgood)
#check box mediaplayers
    def mediaplayershomeen(self):
        if self.mediaplayers.isChecked() == True:
            setuppage.listgood.append("Media Players")
            print(setuppage.listgood)
        else:
            if "Media Players" in setuppage.listgood:
                setuppage.listgood.remove("Media Players")
                print(setuppage.listgood)
#check box musicinstruments
    def musicinstrumentshomeen(self):
        if self.musicinstruments.isChecked() == True:
            setuppage.listgood.append("Music Instruments")
            print(setuppage.listgood)
        else:
            if "Music Instruments" in setuppage.listgood:
                setuppage.listgood.remove("Music Instruments")
                print(setuppage.listgood)
#check box otherhomentertainment
    def otherhomeentertainmenthomeen(self):
        if self.otherhomeentertainment.isChecked() == True:
            setuppage.listgood.append("Other Home Entertainment")
            print(setuppage.listgood)
        else:
            if "Other Home Entertainment" in setuppage.listgood:
                setuppage.listgood.remove("Other Home Entertainment")
                print(setuppage.listgood)

################## The end of Home Entertainment section ###########################

#check box microwaveoven
    def microwaveovenhomeapp(self):
        if self.microwaveoven.isChecked() == True:
            setuppage.listgood.append("Microwave&Oven")
            print(setuppage.listgood)
        else:
            if "Microwave&Oven" in setuppage.listgood:
                setuppage.listgood.remove("Microwave&Oven")
                print(setuppage.listgood)
#check box fan
    def fanhomeapp(self):
        if self.fan.isChecked() == True:
            setuppage.listgood.append("Fan")
            print(setuppage.listgood)
        else:
            if "Fan" in setuppage.listgood:
                setuppage.listgood.remove("Fan")
                print(setuppage.listgood)
#check box refrigerator
    def refrigeratorhomeapp(self):
        if self.refrigerator.isChecked() == True:
            setuppage.listgood.append("Refrigerator")
            print(setuppage.listgood)
        else:
            if "Refrigerator" in setuppage.listgood:
                setuppage.listgood.remove("Refrigerator")
                print(setuppage.listgood)
#check box airconditioner
    def airconditionerhomeapp(self):
        if self.airconditioner.isChecked() == True:
            setuppage.listgood.append("Air Conditioner")
            print(setuppage.listgood)
        else:
            if "Air Conditioner" in setuppage.listgood:
                setuppage.listgood.remove("Air Conditioner")
                print(setuppage.listgood)
#check box airpurifier
    def airpurifierhomeapp(self):
        if self.airpurifier.isChecked() == True:
            setuppage.listgood.append("Air Purifier")
            print(setuppage.listgood)
        else:
            if "Air Purifier" in setuppage.listgood:
                setuppage.listgood.remove("Air Purifier")
                print(setuppage.listgood)
#check box vacuumcleaner
    def vacuumcleanerhomeapp(self):
        if self.vacuumcleaner.isChecked() == True:
            setuppage.listgood.append("Vacuum Cleaner")
            print(setuppage.listgood)
        else:
            if "Vacuum Cleaner" in setuppage.listgood:
                setuppage.listgood.remove("Vacuum Cleaner")
                print(setuppage.listgood)
#check box washingmachine
    def washingmachinehomeapp(self):
        if self.washingmachine.isChecked() == True:
            setuppage.listgood.append("Washing Machine")
            print(setuppage.listgood)
        else:
            if "Washing Machine" in setuppage.listgood:
                setuppage.listgood.remove("Washing Machine")
                print(setuppage.listgood)
#check box otherhomeappliances
    def otherhomeapplianceshomeapp(self):
        if self.otherhomeappliances.isChecked() == True:
            setuppage.listgood.append("Other Home Appliances")
            print(setuppage.listgood)
        else:
            if "Other Home Appliances" in setuppage.listgood:
                setuppage.listgood.remove("Other Home Appliances")
                print(setuppage.listgood)

################## The end of Home Appliances section ###########################

#check box fitness
    def fitnesssports(self):
        if self.fitness.isChecked() == True:
            setuppage.listgood.append("Fitness")
            print(setuppage.listgood)
        else:
            if "Fitness" in setuppage.listgood:
                setuppage.listgood.remove("Fitness")
                print(setuppage.listgood)
#check box campinggears
    def campinggearssports(self):
        if self.campinggears.isChecked() == True:
            setuppage.listgood.append("Camping Gears")
            print(setuppage.listgood)
        else:
            if "Camping Gears" in setuppage.listgood:
                setuppage.listgood.remove("Camping Gears")
                print(setuppage.listgood)
#check box fishing
    def fishingsports(self):
        if self.fishing.isChecked() == True:
            setuppage.listgood.append("Fishing")
            print(setuppage.listgood)
        else:
            if "Fishing" in setuppage.listgood:
                setuppage.listgood.remove("Fishing")
                print(setuppage.listgood)
#check box climbinggears
    def climbinggearssports(self):
        if self.climbinggears.isChecked() == True:
            setuppage.listgood.append("Climbing Gears")
            print(setuppage.listgood)
        else:
            if "Climbing Gears" in setuppage.listgood:
                setuppage.listgood.remove("Climbing Gears")
                print(setuppage.listgood)
#check box skateboards
    def skateboardssports(self):
        if self.skateboards.isChecked() == True:
            setuppage.listgood.append("Skateboards")
            print(setuppage.listgood)
        else:
            if "Skateboards" in setuppage.listgood:
                setuppage.listgood.remove("Skateboards")
                print(setuppage.listgood)
#check box scooters
    def scooterssports(self):
        if self.scooters.isChecked() == True:
            setuppage.listgood.append("Scooters")
            print(setuppage.listgood)
        else:
            if "Scooters" in setuppage.listgood:
                setuppage.listgood.remove("Scooters")
                print(setuppage.listgood)
#check box football
    def footballsports(self):
        if self.football.isChecked() == True:
            setuppage.listgood.append("Football")
            print(setuppage.listgood)
        else:
            if "Football" in setuppage.listgood:
                setuppage.listgood.remove("Football")
                print(setuppage.listgood)                
#check box basketball
    def basketballsports(self):
        if self.basketball.isChecked() == True:
            setuppage.listgood.append("Basketball")
            print(setuppage.listgood)
        else:
            if "Basketball" in setuppage.listgood:
                setuppage.listgood.remove("Basketball")
                print(setuppage.listgood)
#check box tennis
    def tennissports(self):
        if self.tennis.isChecked() == True:
            setuppage.listgood.append("Tennis")
            print(setuppage.listgood)
        else:
            if "Tennis" in setuppage.listgood:
                setuppage.listgood.remove("Tennis")
                print(setuppage.listgood)
#check box badminton
    def badmintonsports(self):
        if self.badminton.isChecked() == True:
            setuppage.listgood.append("Badminton")
            print(setuppage.listgood)
        else:
            if "Badminton" in setuppage.listgood:
                setuppage.listgood.remove("Badminton")
                print(setuppage.listgood)
#check box tabletennis
    def tabletennissports(self):
        if self.tabletennis.isChecked() == True:
            setuppage.listgood.append("Table Tennis")
            print(setuppage.listgood)
        else:
            if "Table Tennis" in setuppage.listgood:
                setuppage.listgood.remove("Table Tennis")
                print(setuppage.listgood)
#check box baseball
    def baseballsports(self):
        if self.baseball.isChecked() == True:
            setuppage.listgood.append("Baseball")
            print(setuppage.listgood)
        else:
            if "Baseball" in setuppage.listgood:
                setuppage.listgood.remove("Baseball")
                print(setuppage.listgood)
#check box divinggears
    def divinggearssports(self):
        if self.divinggears.isChecked() == True:
            setuppage.listgood.append("Diving Gears")
            print(setuppage.listgood)
        else:
            if "Diving Gears" in setuppage.listgood:
                setuppage.listgood.remove("Diving Gears")
                print(setuppage.listgood)
#check box surf
    def surfsports(self):
        if self.surf.isChecked() == True:
            setuppage.listgood.append("Surf")
            print(setuppage.listgood)
        else:
            if "Surf" in setuppage.listgood:
                setuppage.listgood.remove("Surf")
                print(setuppage.listgood)
#check box bicyclegears
    def bicyclegearssports(self):
        if self.bicyclegears.isChecked() == True:
            setuppage.listgood.append("Bicycle Gears")
            print(setuppage.listgood)
        else:
            if "Bicycle Gears" in setuppage.listgood:
                setuppage.listgood.remove("Bicycle Gears")
                print(setuppage.listgood)
#check box golf
    def golfsports(self):
        if self.golf.isChecked() == True:
            setuppage.listgood.append("Golf")
            print(setuppage.listgood)
        else:
            if "Golf" in setuppage.listgood:
                setuppage.listgood.remove("Golf")
                print(setuppage.listgood)
#check box rugby
    def rugbysports(self):
        if self.rugby.isChecked() == True:
            setuppage.listgood.append("Rugby")
            print(setuppage.listgood)
        else:
            if "Rugby" in setuppage.listgood:
                setuppage.listgood.remove("Rugby")
                print(setuppage.listgood)
#check box othersportsoutdoors
    def otherbags_2sports(self):
        if self.otherbags_2.isChecked() == True:
            setuppage.listgood.append("Other Sports&Outdoors")
            print(setuppage.listgood)
        else:
            if "Other Sports&Outdoors" in setuppage.listgood:
                setuppage.listgood.remove("Other Sports&Outdoors")
                print(setuppage.listgood)

################## The end of Sports&Outdoors section ###########################

#check box others
    def otherszzz(self):
        if self.others.isChecked() == True:
            setuppage.listgood.append("Others")
            print(setuppage.listgood)
        else:
            if "Others" in setuppage.listgood:
                setuppage.listgood.remove("Others")
                print(setuppage.listgood)

    #load image
    def loadimage(self):
        global baseimagereal
        try:
            file = QFileDialog.getOpenFileName(self, 'Open File', 'c:', 'Image Files (*.png *.jpg *gif)')
            image_path = file[0]
            pixmap = QPixmap(image_path)
            puxmap = pixmap.scaled(183,183)
            self.displayimage.setPixmap(QPixmap(puxmap))
            baseimage = open(image_path, 'rb')#rb because it's binary data
            baseimagereal = baseimage.read() #will be used to save when the user click done
        except:
            pass
        #self.baseimage.setText(baseimagereal)
    #back to first page
    def goback(self):
        setuppage.listgood = []
        back = Firstpage()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #change second combobox according to first combobox
    def realtag(self):
        listclothes = ["Pajamas","Tank Tops","Sports Sweaters","Suit Jackets","Leather Jackets","Overcoats","T-Shirts","Shirts","Hoodies","Sweaters","Polo Shirts","Dresses","Cropped Shirts","Jeans","Work Pants","Shorts","Sports Pants","Suit Pants","Skirts","Sports Shorts","Leggings","Leather Pants","Fitted Suit Pants","Other Clothes"]
        listshoes = ["Boots","High Heel Boots","Sneakers","Skate Shoes","Flip-Flops","Running Shoes","Sport Shoes","Smart Shoes","Sandals","Slip-Ons","Other Shoes"]
        listaccessories = ["Chains","Earrings","Scarves","Ties","Bangles","Leather Straps","Necklaces","Watches","Gloves","Cuffs","Suspenders","Hats","Glasses","Other Accessories"]
        listmobile =  ["Earphones","Cables&Chargers","Powerbank","Tablet","Cases&Covers","Screen Protector","Mobile Phones","Other Mobile Gadgets"]
        listcom = ["Laptop","Mouse&Keyboard","Headphones","Speakers","Microphones","Printers","Monitors","Computers","Cables","Chargers","Other Computers&Laptop"]
        listbags = ["Backpack&Waist Bags","Clutch&Handheld Bags","Crossbody&Shoulder Bags","Athletic Bags","Luggage&Trunks","Wallets&Purses","Leather Goods","Other Bags"]
        listsport = ["Fitness","Camping Gears","Fishing","Climbing Gears","Skateboards","Scooters","Football","Basketball","Tennis","Badminton","Table Tennis","Baseball","Diving Gears","Surf","Bicycle Gears","Golf","Rugby","Other Sports&Outdoors",]
        listcamera = ["Cameras","Action Cameras","Film","Lens","CCTV","Additional Gears","Other Cameras"]
        listhomeen = ["TV","Projectors","Media Players","Music Instruments","Other Home Entertainment"]
        listhomeapp = ["Microwave&Oven","Fan","Refrigerator","Air Conditioner","Air Purifier","Vacuum Cleaner","Washing Machine","Other Home Appliances"]
        listgames = ["Discs&Cartridges","Gaming Gears","Collectibles","Souvenirs","Board Games","Other Games"]

        bigtag = self.mytag.currentText()
        if bigtag == "Clothes":
            self.smalltag.clear()
            for i in listclothes:
                self.smalltag.addItem(i)
        elif bigtag == "Shoes":
            self.smalltag.clear()
            for i in listshoes:
                self.smalltag.addItem(i)
        elif bigtag == "Bags":
            self.smalltag.clear()
            for i in listbags:
                self.smalltag.addItem(i)
        elif bigtag == "Accessories":
            self.smalltag.clear()
            for i in listaccessories:
                self.smalltag.addItem(i)
        elif bigtag == "Mobile Gadgets":
            self.smalltag.clear()
            for i in listmobile:
                self.smalltag.addItem(i)
        elif bigtag == "Computers&Laptops":
            self.smalltag.clear()
            for i in listcom:
                self.smalltag.addItem(i)
        elif bigtag == "Cameras":
            self.smalltag.clear()
            for i in listcamera:
                self.smalltag.addItem(i)
        elif bigtag == "Games":
            self.smalltag.clear()
            for i in listgames:
                self.smalltag.addItem(i)
        elif bigtag == "Home Entertainment":
            self.smalltag.clear()
            for i in listhomeen:
                self.smalltag.addItem(i)
        elif bigtag == "Home Appliances":
            self.smalltag.clear()
            for i in listhomeapp:
                self.smalltag.addItem(i)
        elif bigtag == "Sports&Outdoors":
            self.smalltag.clear()
            for i in listsport:
                self.smalltag.addItem(i)
        elif bigtag == "Others":
            self.smalltag.clear()
            self.smalltag.addItem("Others")
#DONE         
class deletepage(QDialog):
    def __init__(self):
        super(deletepage, self).__init__()
        loadUi("deletepage.ui", self)
        self.gobackfromdelete.clicked.connect(self.goback)
        self.deletebutton.clicked.connect(self.delete)
    #back to first page
    def goback(self):
        back = Firstpage()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)
    #delete account done
    def delete(self):
        proid = self.productid.text()
        password = self.password.text()
        if proid == "" or password == "":
            self.errormessage.setText("Input all fields")
        else:
            connect = sqlite3.connect("account.db")
            cur = connect.cursor()
            query = 'SELECT productpassword FROM login WHERE productID =\''+proid+"\'"
            cur.execute(query)
            try:
                result = cur.fetchone()[0]
                if result == password:
                    newquery = 'DELETE FROM login WHERE productID =\''+proid+"\'"
                    cur.execute(newquery)
                    connect.commit()
                    connect.close()
                    match = Firstpage()
                    widget.addWidget(match)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    self.errormessage.setText("Invalid password")
            except:
                self.errormessage.setText("Account does not exist")

app = QApplication(sys.argv) #execute script
first = Firstpage()
widget = QtWidgets.QStackedWidget() 
widget.addWidget(first) #add and set up the first page
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
sys.exit(app.exec_()) #exit python
