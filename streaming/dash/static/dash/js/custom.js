var manifestUri = "/static/dash/media/live.mpd";

function initDash() {
  var player = dashjs.MediaPlayer().create();
  player.initialize(document.getElementById("dashjs-player"),
                    manifestUri, true);
  player.clearDefaultUTCTimingSources();
};

initDash();
