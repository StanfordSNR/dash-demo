const LOG_PREFIX = 'VIDEO_EVENT';

/* Wrap the builtin log function */
var orig_console_log = console.log;
console.log = function(...args) {
  orig_console_log.apply(this, args);
};

var video = document.getElementById('dashjs-player');
var start_time = Date.now();
function get_time() {
  return Date.now() - start_time;
};

video.onpause = function(e) {
  console.log(LOG_PREFIX + ' pause ' + get_time(), e);
};

video.onplay = function(e) {
  console.log(LOG_PREFIX + ' play ' + get_time(), e);
};

video.oncanplay = function(e) {
  console.log(LOG_PREFIX + ' canplay ' + get_time(), e);
};

video.onwaiting = function(e) {
  console.log(LOG_PREFIX + ' waiting ' + get_time(), e);
};

video.onloadstart = function(e) {
  console.log(LOG_PREFIX + ' loadstart ' + get_time(), e);
};

video.onstalled = function(e) {
  console.log(LOG_PREFIX + ' stalled ' + get_time(), e);
};
