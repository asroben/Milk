<?xml version="1.0" encoding="UTF-8"?>
<%
String audioListCSV = "";
File[] audioList = new File("/provisioned/music/").listFiles();
for (int i = 0; i < audioList.length; ++i) {
    File audio = audioList[i];
    if (audio.isFile()) {
        audioListCSV += "\'file:///" + audio.getAbsolutePath() + "\'";
        if (i + 1 < audioList.length) {
            audioListCSV += ",";
        }
    }
}
%>    
<vxml version="2.1">
    <form>
        <block>
            <var name="audioList" />
            <assign name="audioList" expr="[<%=audioListCSV%>]" />
            <return namelist="audioList" />
        </block>
    </form>
</vxml>