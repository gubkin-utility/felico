import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.2
import QtQuick.Dialogs 1.2
import QtQuick.Layouts 1.2
import QtGraphicalEffects 1.0
import QtMultimedia 5.0



Window {
    maximumWidth: 640
    maximumHeight: 480
    minimumWidth: maximumWidth
    minimumHeight: maximumHeight

    visible: true
    id: root
    title: qsTr("Felico")


    property string file_zagotovka: ""
    //ТЕСТ НА ПРАВИЛЬНОСТЬ КОДИРОВКИ
    property string file_coding_status: ""
    property string file_zamena: ""

    Audio {
            id: sound_click
            source: "sound/click_button.wav"
            volume: 0.1
        }



    GridLayout {
        anchors.fill: parent
        rows: 1
        columns: 3

        Rectangle {
            color: "#555c80"
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.column: 1
            Layout.row: 1


            Column {
                anchors.centerIn: parent
                spacing: 10

                //logotip
                Text {
                    id: text_logo
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "Felico"
                    font.pixelSize: 50
                    smooth: true
                    color: "orange"
                    font.family: font_logo.name

                    FontLoader {
                        id: font_logo
                        source: "fonts/Rurintania.ttf"
                    }

                }


                Ramka {
                    width: 300
                    height: 60
                    title: "файл со строками для замены: "

                    Button {
                        text: "обзор"
                        anchors.centerIn: parent
                        style: ButtonStyle {
                            label: Text {
                                renderType: Text.NativeRendering
                                verticalAlignment: Text.AlignVCenter
                                horizontalAlignment: Text.AlignHCenter
                                font.pointSize: 12
                                font.family: font_pathfolder.name
                                color: control.pressed ? "white" : "black"
                                text: control.text
                            }
                            background: Rectangle {
                                implicitWidth: 150
                                implicitHeight: 10
                                border.width: 1
                                border.color: "grey"
                                radius: 10
                                color: control.hovered ? "#84af27" : "transparent"
                            }

                        }



                        FileDialog {
                            id: filedial_zamena
                            title: "Выбирите файл со строками для замены"
                            visible: false
                            modality: Qt.WindowModal
                            nameFilters: ["Doc(*.txt)" , "All file(*)"]
                            onAccepted: {
                                standart.test_codirovka(filedial_zamena.fileUrl)
                                if(file_coding_status === "False"){
                                    page_error.title = "Ошибка"
                                    page_error.text = "Кодировка файла не UTF-8 !"
                                    page_error.visible = true

                                }
                                else {
                                file_zamena = filedial_zamena.fileUrl
                                text_filezamena.text = file_zamena
                                //to py script
                                standart.make_path(filedial_zamena.fileUrl)
                                }
                            }
                        }

                        onClicked: {

                            filedial_zamena.visible = true
                            sound_click.play()

                        }

                    }

                    FontLoader {
                        id: font_pathfolder
                        source: "fonts/2.ttf"
                    }

                    Text {
                        id: text_filezamena
                        width: 285
                        //height: 30
                        anchors.right: parent.right
                        anchors.bottom: parent.bottom
                        anchors.margins: 5
                        elide: Text.ElideLeft
                        text: ""
                        color: "#f9b76b"
                        font.family: font_pathfolder.name
                    }

                }


                Ramka {
                    width: 300
                    height: 60
                    title: "файл заготовка: "



                Button {
                    anchors.centerIn: parent
                    text: "обзор"
                    style: ButtonStyle {
                        label: Text {
                            renderType: Text.NativeRendering
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                            font.pointSize: 12
                            font.family: font_pathfolder.name
                            color: control.pressed ? "white" : "black"
                            text: control.text
                        }
                        background: Rectangle {
                            implicitWidth: 150
                            implicitHeight: 10
                            border.width: 1
                            border.color: "grey"
                            radius: 10
                            color: control.hovered ? "#84af27" : "transparent"
                        }

                    }

                        FileDialog {
                            id: filedial_zagotovka
                            title: "Выбирите файл заготовку"
                            visible: false
                            modality: Qt.WindowModal
                            nameFilters: ["Doc(*.txt)" , "All file(*)"]
                            onAccepted: {
                                standart.test_codirovka(filedial_zagotovka.fileUrl)
                                if(file_coding_status === "False"){
                                    page_error.title = "Ошибка"
                                    page_error.text = "Кодировка файла не UTF-8 !"
                                    page_error.visible = true

                                }
                                else {
                                file_zagotovka = filedial_zagotovka.fileUrl
                                text_filezagotovka.text = file_zagotovka
                                //to py script
                                standart.make_path(filedial_zagotovka.fileUrl)
                                }
                            }


                        }

                        onClicked: {

                            filedial_zagotovka.visible = true
                            sound_click.play()

                        }


                    }

                    Text {
                        id: text_filezagotovka
                        width: 285
                        anchors.right: parent.right
                        anchors.bottom: parent.bottom
                        anchors.margins: 5
                        elide: Text.ElideLeft
                        text: ""
                        color: "#f9b76b"
                        font.family: font_pathfolder.name
                    }

                    //from py script
                    Connections {
                        target: standart
                        function onModPath(modpath) {
                            label_finalpath.text = modpath
                        }}

                    Connections {
                        target: standart
                        function onNowProgbar(nowprogbar) {
                            progress_1.value = nowprogbar
                        }
                        function onMaxProgbar(maxprogbar) {
                            progress_1.maximumValue = maxprogbar
                        }
                        function onAllOk(status) {
                            page_error.title = "Ok"
                            page_error.text = "Выполнено"
                            page_error.visible = true
                        }
                        function onForTectcoding(status) {
                            file_coding_status = status
                        }

                    }


                }

                //путь к финальному файлу
                Ramka {
                    width: 300
                    height: 60
                    title: "путь к финальному файлу: "

                    Text {
                        id: label_finalpath
                        width: 285
                        anchors.centerIn: parent
                        anchors.margins: 5
                        text: ""
                        elide: Text.ElideLeft
                        font.family: font_pathfolder.name
                        font.pointSize: 12
                        color: "#15f54e"

                    }
                }

                //символ для замены
                Ramka {
                    width: 300
                    height: 60
                    title: "символ для замены"

                    TextField {
                        id: textfiled_symbol
                        width: 200
                        height: 30
                        anchors.centerIn: parent
                        text: "*"
                    }
                }

                //button srart stop
                Item {
                    height: 2
                    width: 10
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    anchors.horizontalCenter: parent.horizontalCenter
                    width: 210
                    height: 50
                    radius: 10

                    ProgressBar {
                        id: progress_1
                        anchors.fill: parent
                        value: 0
                        minimumValue: 0
                        maximumValue: 10
                        style: ProgressBarStyle {
                            background: Rectangle {
                                radius: 10
                                color:"lightgray"
                                border.color: "yellow"
                                border.width: 3


                            }
                            progress: Rectangle {
                                color:"lightsteelblue"
                                border.color: "#fff3bf"
                                radius: 10


                            }

                        }

                        Text {
                            id: text_progbar
                            anchors.centerIn: parent
                            text: progress_1.value === 0 ? "пуск":"стоп"
                            font.family: font_pathfolder.name
                            font.pointSize: 30
                            color: "#544c80"
                        }

                        MessageDialog {
                            id: page_error
                            visible: false
                            standardButtons: MessageDialog.Ok
                            icon: StandardIcon.Question

                    }

                        MouseArea {
                            anchors.fill: parent
                            onClicked: {

                                sound_click.play()

                                if(text_progbar.text === "stop"){
                                    standart.running = False

                                }

                                else if(text_filezamena.text.length === 0){
                                    page_error.title = "Ошибка"
                                    page_error.text = "Не выбран файл <p>\"со строками для замены\" !</p>"
                                    page_error.visible = true
                                }
                                else if (text_filezagotovka.text.length === 0){
                                    page_error.title = "Ошибка"
                                    page_error.text = "Не выбран файл <p>\"заготовка\"</p>"
                                    page_error.visible = true
                                }


                                else if (textfiled_symbol.text.length === 0){
                                    page_error.title = "Ошибка"
                                    page_error.text = "Не выбран <p>\"символ для замены\" !</p>"
                                    page_error.visible = true
                                }


                                else if (text_filezamena.text === text_filezagotovka.text){
                                    page_error.title = "Ошибка"
                                    page_error.text = "Выбрано два одинаковых файла !"
                                    page_error.visible = true
                                }



                                else {standart.felico(text_filezamena.text, text_filezagotovka.text,label_finalpath.text, textfiled_symbol.text)
                                }
                            }


                        }
                    }
                }



            }
        }


        //right column
        Rectangle {
            color: "red"
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.column: 2
            Layout.row: 1


            Column {
                anchors.fill: parent
                anchors.centerIn: parent
                spacing: 1


                Item {
                    width: 10
                    height: 10

                }


                Button {
                    id: btn_clear
                    anchors.right: parent.right
                    anchors.rightMargin: 10
                    iconSource: "img/clear.png"
                    style: ButtonStyle {
                        background: Rectangle {
                        implicitWidth: 15
                        implicitHeight: 15
                        border.width: 2
                        opacity: enabled ? 1:0.3
                        border.color: btn_clear.pressed ? "pink" : "yellow"
                        radius: 50
                        color: btn_clear.hovered ? "white" : "transparent"
                        }
                    }
                    onClicked: {
                        sound_click.play()
                        root.close()
                    }
                }


                Text {
                    anchors.left: parent.left
                    anchors.leftMargin: 10
                    font.family: font_pathfolder.name
                    font.pixelSize: 10
                    color: "black"

                    text: {
                        "
                        <p><font size=\"6\" color=\"navy\">ОБРАЗЕЦ:</font></p>

                        <p><font size=\"5\">файл со строками для замены txt ---></font></p>
                        <p>Москва</p>
                        <p>Санкт-Петербург</p>

                        <p><font size=\"5\">файл заготовка txt ---></font></p>
                        <p>купить самокат Ninebot *</p>
                        <p>купить самокат Xiaomi *</p>
                        <p>купить самокат Kugoo *</p>

                        <p><font size=\"5\">Результат: финальный файл txt ---></font></p>
                        <p>купить самокат Ninebot Москва</p>
                        <p>купить самокат Xiaomi Москва</p>
                        <p>купить самокат Kugoo Москва</p>
                        <p>купить самокат Ninebot Санкт-Петербург</p>
                        <p>купить самокат Xiaomi Санкт-Петербург</p>
                        <p>купить самокат Kugoo Санкт-Петербург</p>
                        "


                    }
                }





                MessageDialog {
                    id: page_about
                    title: "Об программе"
                    visible: false
                    standardButtons: MessageDialog.Ok
                    informativeText: {
                        '<p><font color="navy" face="arial" size="3"><b>Felico</b></font> - программа для размножения ключевых слов</p>

                         <p>версия: 2.0</p>

                         <p>лицензия: Donationware</p>

                         <p>donate: <a href="https://gubkin-utility.github.io/felico/page/donate.html">Donation Link </a></p>

                         <p>автор: <a href="https://www.facebook.com/leonid.gubkin">Leonid Gubkin</a></p>

                         <p>сайт: <a href="https://gubkin-utility.github.io/felico/">Felico Web</a></p>


                         <p>This program comes with absolutely no warranty<br>(эта программа не имеет никаких гарантий)</p>
                         '
                    }
                }



                Button {
                    id: btn_about
                    anchors.right: parent.right
                    anchors.rightMargin: 10
                    iconSource: "img/about.png"
                    style: ButtonStyle {
                        background: Rectangle {
                        implicitWidth: 15
                        implicitHeight: 15
                        border.width: 2
                        opacity: enabled ? 1:0.3
                        border.color: btn_about.pressed ? "pink" : "yellow"
                        radius: 50
                        color: btn_about.hovered ? "white" : "transparent"
                        }
                    }
                    onClicked: {
                        sound_click.play()
                        page_about.open()
                    }
                }






                Item {
                    width: 10
                    height: 10
                }






            }
        }

    }



}
