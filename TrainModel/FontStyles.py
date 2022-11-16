#This file sets up the fonts and stylesheets that the widgets will use
from PyQt6.QtGui import QFont 

section_font = QFont("Helvetica", 23);
section_font.setUnderline(True)
section_font.setBold(True)
section_label_stylesheet = "QLabel { color : rgb(221, 221, 221); }"

time_font = QFont("Helvetica", 15)
time_font.setBold(True)
time_label_stylesheet = "QLabel { color : rgb(255, 255, 255); } QLabel:Disabled { color : rgb(140, 140, 140); }"

normal_font = QFont("Helvetica", 12)
normal_font.setBold(True)
normal_label_stylesheet = "QLabel { color : rgb(221, 221, 221); } QLabel:Disabled { color : rgb(140, 140, 140); }"

small_font = QFont("Helvetica", 9)
small_font.setBold(True)

speed_button_stylesheet = '''QPushButton { background-color : rgb(255, 255, 255); 
										 color : rgb(0, 0, 0);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}'''

selected_speed_button_stylesheet = '''QPushButton { background-color : rgb(92, 149, 230); 
										 color : rgb(0, 0, 0);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}'''

black_button_stylesheet = '''QPushButton { background-color : rgb(0, 0, 0); 
										 color : rgb(255, 255, 255);
										 border: 3px solid rgb(130, 130, 130);
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}
						 QPushButton:hover { background-color: rgb(50, 50, 50);}
						 QPushButton:pressed { background-color: rgb(100, 100, 100);}
						 QPushButton:disabled { background-color: rgb(170, 170, 170);
											color: rgb(100, 100, 100);
											border-color: rgb(100, 100, 100);}'''

light_red_button_stylesheet = '''QPushButton { background-color : rgb(255, 160, 160); 
										 color : rgb(0, 0, 0);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}
						 QPushButton:hover { background-color: rgb(225, 145, 145);}
						 QPushButton:pressed { background-color: rgb(210, 120, 120);}
						 QPushButton:disabled { background-color: rgb(170, 170, 170);
											color: rgb(100, 100, 100);
											border-color: rgb(100, 100, 100);}'''
											
										 
red_button_stylesheet = '''QPushButton { background-color : rgb(207, 42, 39); 
										 color : rgb(255, 255, 255);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}
						 QPushButton:hover { background-color: rgb(160, 30, 29);}
						 QPushButton:pressed { background-color: rgb(130, 20, 19);}
						 QPushButton:disabled { background-color: rgb(170, 170, 170);
											color: rgb(100, 100, 100);
											border-color: rgb(100, 100, 100);}'''
						 
dark_red_button_stylesheet = '''QPushButton { background-color : rgb(102, 0, 0); 
										 color : rgb(255, 255, 255);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}
						 QPushButton:hover { background-color: rgb(70, 0, 0);}
						 QPushButton:pressed { background-color: rgb(45, 0, 0); }
						 QPushButton:disabled { background-color: rgb(170, 170, 170);
											color: rgb(100, 100, 100);
											border-color: rgb(100, 100, 100);}'''
						 
yellow_button_stylesheet = '''QPushButton { background-color : rgb(255, 255, 0); 
										 color : rgb(0, 0, 0);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}
						 QPushButton:hover { background-color: rgb(210, 210, 0);}
						 QPushButton:pressed { background-color: rgb(170, 170, 0); }'''
                     
green_button_stylesheet = '''QPushButton { background-color : rgb(42, 160, 39); 
										 color : rgb(255, 255, 255);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}
						 QPushButton:hover { background-color: rgb(30, 130, 29);}
						 QPushButton:pressed { background-color: rgb(20, 100, 19);}
						 QPushButton:disabled { background-color: rgb(170, 170, 170);
											color: rgb(100, 100, 100);
											border-color: rgb(100, 100, 100);}'''
											
blue_button_stylesheet = '''QPushButton { background-color : rgb(43, 120, 228); 
										 color : rgb(255, 255, 255);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}
						 QPushButton:hover { background-color: rgb(27, 95, 198);}
						 QPushButton:pressed { background-color: rgb(17, 67, 165);}
						 QPushButton:disabled { background-color: rgb(170, 170, 170);
											color: rgb(100, 100, 100);
											border-color: rgb(100, 100, 100);}'''

dark_purple_button_stylesheet = '''QPushButton { background-color : rgb(103, 78, 167); 
										 color : rgb(255, 255, 255);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}
						 QPushButton:hover { background-color: rgb(77, 62, 137);}
						 QPushButton:pressed { background-color: rgb(60, 43, 110);}'''

purple_button_stylesheet = '''QPushButton { background-color : rgb(153, 0, 255); 
										 color : rgb(255, 255, 255);
										 border: 3px solid black;
										 padding-left: 10px;
										 padding-right: 10px;
										 padding-top: 3px;
										 padding-bottom: 3px;}
						 QPushButton:hover { background-color: rgb(123, 0, 200);}
						 QPushButton:pressed { background-color: rgb(95, 0, 160);}'''
                     
gold_button_stylesheet = '''QPushButton { background-color : rgb(241, 194, 50); 
                                     color : rgb(0, 0, 0);
                                     border: 3px solid black;
                                     padding-left: 10px;
                                     padding-right: 10px;
                                     padding-top: 3px;
                                     padding-bottom: 3px;}
                     QPushButton:hover { background-color: rgb(200, 154, 30);}
                     QPushButton:pressed { background-color: rgb(170, 124, 20); }
                     QPushButton:disabled { background-color: rgb(170, 170, 170);
											color: rgb(100, 100, 100);
											border-color: rgb(100, 100, 100);}'''
                     
 

radio_stylesheet = '''QRadioButton {
                                    color: rgb(221,221,221);
                                    }

                                    QRadioButton::indicator::unchecked{ 
                                    border: 1px solid; 
                                    border-color: rgb(221,221,221);
                                    border-radius: 5px;
                                    background-color: rgb(102, 102, 102); 
                                    }

                                    QRadioButton::indicator::checked{ 
                                    border: 1px solid; 
                                    border-color: rgb(221,221,221);
                                    border-radius: 5px;
                                    background-color: rgb(221, 221, 221); 
                                    }'''

entry_stylesheet = '''QLineEdit {border: 3px solid black}'''

red_entry_stylesheet = '''QLineEdit {border: 3px solid rgb(255, 42, 39)}'''
                                    
table_stylesheet = '''QTableWidget {alternate-background-color: rgb(51, 51, 51); 
                                    background-color: rgb(90, 90, 90);
                                    gridline-color: black;
                                    outline: 0;
                                    border: 3px solid black}
                      QHeaderView::section {background-color: rgb(170, 170, 170);}
                      QTableView::item {border: 1px solid black;
                                        color: rgb(221,221,221);}
                      QTableView::item:selected{background-color : rgb(92, 149, 230);
                                                 selection-color : #000000;}
					 QTableView {alternate-background-color: rgb(51, 51, 51); 
                                    background-color: rgb(90, 90, 90);
                                    gridline-color: black;
                                    outline: 0;
                                    border: 3px solid black}
                      QHeaderView::section {background-color: rgb(170, 170, 170);}
                      QTableView::item {border: 1px solid black;
                                        color: rgb(221,221,221);}
                      QTableView::item:selected{background-color : rgb(92, 149, 230);
                                                 selection-color : #000000;}
					  QToolTip {background-color: rgb(102, 102, 102); 
							    color: rgb(221, 221, 221);
							    font-size: 15px;
							    font-family: Helvetica;
							    font-weight: bold;
                                border: 0px solid black;}'''
