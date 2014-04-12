#!/usr/bin/python
# -*- coding: utf-8 -*-

import traceback
import sys

import cs_moves
import cs_player

from PySide import QtCore, QtGui
from PySide.QtGui import QShortcut, QKeySequence

from gamewindow import Ui_GameWindow
from mainwindow import Ui_MainWindow

def message(text):
    msgBox = QtGui.QMessageBox()
    msgBox.setText(text)
    msgBox.exec_()

def solveHalts(move_list):
    """Put all halts into a list and then loop over it,
    Executing any halts that are not themselves halted and
    removing them and their targets, repeating until all halts have been
    removed or the loop has executed enough to prove that
    all remaining halts are in stable halt-loops, and discarded.
    """
    def halted(target, halts):
        halters = []
        for halt in halts:
            if halt.target == target:
                halters.append(halt)
        return halters

    halt_list = []
    for move in move_list:
        if isinstance(move, cs_moves.Halt):
            halt_list.append(move)

    loops = 0
    while len(halt_list) > 0 and loops < len(move_list):
        # All halts that are not themselves halted proceed
        # Any halts that they were halting cannot resolve
        for halt in halt_list:
            halter = halted(halt.player, halt_list)
            if not halter:
                halt.halt()
                for target_halt in halt_list:
                    if target_halt.player == halt.target:
                        halt_list.remove(target_halt)
                halt_list.remove(halt)
        loops += 1
    for halt in halt_list:
        move_list.remove(halt)

class CrossGame(QtGui.QMainWindow):
    def closeEvent(self, event): 
        self.parent.show()
        self.parent.gameEnded()
        event.accept()

    def setupRound(self):
        self.moves = []
        self.moveCount = 0
        for AI in self.AIs:
            if AI.player not in self.dead_players:
                act = AI.act()
                self.moves.append(act)
            self.moveCount += 1
        self.nextPlayer()
        
        # Reset temporary aspects of each player.
        for player in self.players:
            player.newRound()

    def endGame(self):
        # If there is one survivor, they score their own HP
        if len(self.dead_players) < len(self.players):
            for player in self.players:
                if player not in self.dead_players:
                    player.addVP(player.hp)
                    break

        # Find the player with the most VP 
        winner = max(self.players, key=lambda player:player.vp)
        ties = []
        for player in self.players:
            if player.vp == winner.vp:
                ties.append(player)

        # A single winner
        if len(ties) == 1:
            message("The winner is %s, with %d VP!"%(ties[0].name, ties[0].vp))
        # A tie for the most VP
        else:
            winstring = "The winners, with %d VP, are: "%ties[0].vp
            for player in ties:
                winstring += "\n\t%s"%player.name
            message(winstring)
        self.parent.show()
        self.parent.gameEnded()
        self.close()
                

    def processRound(self):
        """Carry out one round of the game by performing the follownig teps:
        -Resolve any HALT loops and HALT moves.
        -Apply the setup for each move, which includes setting up defenses, making sure targets are lunged and focused properly, etc.
        -Resolve each move, dealing out damage.
        -Update the display with the new HP and VP totals of each player
        -Move any player that is dead to the dead players list.
        -Check if we have enough players to continue the game.
        """
        # Print out a list of all of the moves.
        summary = ""
        for move in self.moves:
            summary += "%s used %s on %s\n" %(move.player.name, 
                                              move.name(), 
                                              move.target.name)
        message(summary)

        # Resolve halts.
        solveHalts(self.moves)

        # Setup each move before any of the moves resolve.
        for move in self.moves:
            move.setup()

        # Resolve each move: dealing damage, transfering VP, etc.
        for move in self.moves:
            move.resolve()

        # Update the display
        for i in range(len(self.players)):
            hp = "%d"%max(0, self.players[i].hp)
            vp = "%d"%self.players[i].vp
            self.ui.listPlayer.item(i, 1).setText(hp)
            self.ui.listPlayer.item(i, 2).setText(vp)

        # Collect dead Players
        for player in self.players:
            if player not in self.dead_players and player.hp <= 0:
                self.dead_players.append(player)

        # Check to see if there are enough survivors to continue
        if len(self.dead_players) >= len(self.players) -1:
            self.endGame()
            return

        self.setupRound()

    def nextPlayer(self):
        """Updates the display with the name, HP, and VP of the current player. """
        try:
            current_player = self.players[self.moveCount]
            self.ui.lblName.setText(current_player.name)
            self.ui.lblHP.setText("%d"%current_player.hp)
            self.ui.lblVP.setText("%d"%current_player.vp)
            if current_player in self.dead_players:
                self.cycleTurn()

        except:
            self.cycleTurn()

    @QtCore.Slot()
    def on_btnStrike_clicked(self):self.submit(0)
    @QtCore.Slot()
    def on_btnLunge_clicked(self):self.submit(1)
    @QtCore.Slot()
    def on_btnAssail_clicked(self):self.submit(2)
    @QtCore.Slot()
    def on_btnDodge_clicked(self):self.submit(3)
    @QtCore.Slot()
    def on_btnBlock_clicked(self):self.submit(4)
    @QtCore.Slot()
    def on_btnRiposte_clicked(self):self.submit(5)
    @QtCore.Slot()
    def on_btnTaunt_clicked(self):self.submit(6)
    @QtCore.Slot()
    def on_btnFocus_clicked(self):self.submit(7)
    @QtCore.Slot()
    def on_btnMend_clicked(self):self.submit(8)
    @QtCore.Slot()
    def on_btnHalt_clicked(self):self.submit(9)

    def submit(self, move_id=-1):
        """The user has selected a target and clicked on an move Button.
        Several checks will be done to ensure that the move is valid.
        If it is, it will be added to the list of move and paly will pass to the next player.
        If not, this move will be discarded by leaving the method early.
        If all players have acted, the round's moves will be carried out."""

        index = self.ui.listPlayer.currentRow()
        target = self.players[index]
        if target in self.dead_players:
            message("Apologies, but that player is dead.")
            return
        
        #move_id = -1*(self.ui.btnGroupMoves.checkedId()+2)

        # The user hasn't selected an move.
        if move_id < 0: return 

        # Can't target yourself, except possibly with a Mend move
        if (move_id != cs_moves.MEND and 
            target == self.players[self.moveCount]):
            message("You can't target yourself with that move.")
            return

        
        move = cs_moves.moveList[move_id](self.players[self.moveCount], self.players, target)
        
        self.moves.append(move)

        self.cycleTurn()

    def cycleTurn(self):
        """Increment the move count for this round.
        End the round if it reaches the number of players.
        Otherwise go to the next players"""
        self.moveCount += 1
        if self.moveCount >= len(self.players):
            self.processRound()
        else:
            self.nextPlayer()

    def __init__(self, players, ais, parent=None):
        super(CrossGame, self).__init__()
        self.parent = parent

        # Create the widgets and buttons.
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Crossing Swords")

        # Store each AI player in a list for 
        # easy collection of their moves.
        self.AIs = ais
        
        # Add all the players into one list, with the AI first for easy calculation of turn order.
        self.players_human = players
        self.players_ai = [AI.player for AI in ais]
        self.players = self.players_ai + self.players_human
        self.dead_players = []
        for AI in ais:
            AI.setPlayerListReference(self.players, self.dead_players)
        for player in self.players:
            self.ui.listPlayer.setRowCount(self.ui.listPlayer.rowCount()+1)
            nameItem = QtGui.QTableWidgetItem("%s" %player.name)
            hpItem = QtGui.QTableWidgetItem("%d" %player.hp)
            vpItem = QtGui.QTableWidgetItem("%d" %player.vp)
            self.ui.listPlayer.setItem(self.ui.listPlayer.rowCount()-1, 0, nameItem)
            self.ui.listPlayer.setItem(self.ui.listPlayer.rowCount()-1, 1, hpItem)
            self.ui.listPlayer.setItem(self.ui.listPlayer.rowCount()-1, 2, vpItem)

        self.show()


        self.setupRound()
   

class CrossingSwords(QtGui.QMainWindow):

    def gameEnded(self):
        self.playerModel.clear()
        self.players = []
        self.AIs = []
        cs_player.reset_names()

    @QtCore.Slot()
    def on_btnAddAI_clicked(self):
        self.ui.btnAddAI.setEnabled(False)
        print len(self.players) + len(self.AIs)
        if len(self.players)+len(self.AIs) >= 16:
            self.ui.btnAddAI.setEnabled(True)
            return
        name_ai = "AI%d"%len(self.AIs)
        self.playerModel.appendRow(QtGui.QStandardItem(name_ai))
        self.AIs.append(cs_player.AI())
        self.ui.btnAddAI.setEnabled(True)

    @QtCore.Slot()
    def on_leName_returnPressed(self):
        self.on_btnAddHuman_clicked()
    @QtCore.Slot()
    def on_btnAddHuman_clicked(self):
        if len(self.players)+len(self.AIs) >= 16:
            return
        if len(self.ui.leName.text()) < 1:
            return

        self.playerModel.appendRow(QtGui.QStandardItem(self.ui.leName.text()))
        self.players.append(cs_player.PlayerHuman(self.ui.leName.text()))
        self.ui.leName.setText("")

    @QtCore.Slot()
    def on_btnQuit_clicked(self):
        self.close()

    @QtCore.Slot()
    def on_btnStart_clicked(self):
        if len(self.players) + len(self.AIs) < 2:
            return

        self.game = CrossGame(self.players, self.AIs, self)
        self.game.show()
        self.hide()

    def closeEvent(self, event): 
        event.accept()

    def __init__(self, parent=None):
        super(CrossingSwords, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.playerModel = QtGui.QStandardItemModel()
        self.ui.listPlayer.setModel(self.playerModel)
        
        self.setWindowTitle("Crossing Swords")

        self.players = []
        self.AIs = []

        
if __name__ == '__main__':
    try:
        app = QtGui.QApplication(sys.argv)
        widget = CrossingSwords()

        widget.show()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass
    except SystemExit as e:
        if int("%s"%e) != 0:
            raise
    except:
        print "Exception caught:"
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
