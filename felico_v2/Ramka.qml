import QtQuick 2.0
import QtGraphicalEffects 1.0



Item {
    id: root
    width: 100
    height: 100
    property color border_color: "#e1e879"
    property string title: "title"

    FontLoader {
        id: font_title
        source: "fonts/ariblk.ttf"
    }



    RectangularGlow {
        id: effect
        anchors.fill: thisa
        glowRadius: 10
        spread: 0.2
        color: "white"
        cornerRadius: 25

    }

    Rectangle {
        id: thisa
        anchors.fill: parent
        color: "#555c80"
        border.color: root.border_color
        border.width: 2
        radius: 5
        antialiasing: true
        width: Math.round(parent.width /1.5)
        height: Math.round(parent.height / 3)



        Text {
            anchors.left: parent.left
            anchors.leftMargin: 5
            text: title
            color: "white"
            font.family: font_title.name
            font.pointSize: 7

        }

        MouseArea {
            focus: true
            anchors.fill: parent
            //on: root.color = "orange"
            //onExited: root.color = "purple"
        }



    }

}
