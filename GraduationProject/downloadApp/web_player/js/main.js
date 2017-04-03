'use strict';
angular.module('myApp', 
  [
    "ngSanitize", 
    "com.2fdevs.videogular", 
    "com.2fdevs.videogular.plugins.controls", 
    "com.2fdevs.videogular.plugins.overlayplay", 
    "com.2fdevs.videogular.plugins.poster"
    ])
.controller('HomeCtrl', ["$sce",function($sce) {
  this.config = {
    sources: [{
      // src: $sce.trustAsResourceUrl("http://static.videogular.com/assets/videos/videogular.mp4"),
      // type: "video/mp4"
      src: $sce.trustAsResourceUrl("./media/video/skateboard.mp4"),
      type: "video/mp4"
    },
    {
      src: $sce.trustAsResourceUrl("http://static.videogular.com/assets/videos/videogular.webm"),
      type: "video/webm"
    },
    {
      src: $sce.trustAsResourceUrl("http://static.videogular.com/assets/videos/videogular.ogg"),
      type: "video/ogg"
    }],
    // tracks: [{
    //   src: "http://www.videogular.com/assets/subs/pale-blue-dot.vtt",
    //   kind: "subtitles",
    //   srclang: "en",
    //   label: "English",
    // default:
    //   ""
    // }],
    theme: "bower_components/videogular-themes-default/videogular.css",
    // theme: "http://www.videogular.com/styles/themes/default/latest/videogular.css",
    plugins: {
      poster: "./media/img/logo.png",
      controls: {
        autoHide: true,
        autoHideTime: 5000
      }
    }
  };
  var vm=this;
  vm.searched = false;
  // vm.video_url
  vm.search_video = function() {
    console.log(vm.video_url);
    vm.searched = true;
  }
  vm.success = true;
  vm.videoinfos = [
    {'key': 'site', 'value': 'Youku'},
    {'key': 'title', 'value': 'skateboard'},
    {'key': 'size', 'value': '40M'},
    {'key': 'type', 'value': 'mp4'},
    {'key': 'info', 'value': '日本漂移板神童山本勇 屌炸天了！xxxxxxx日本漂移板神童山本勇 屌炸天了！xxxxxxx日本漂移板神童山本勇 屌炸天了！xxxxxxx日本漂移板神童山本勇 屌炸天了！xxxxxxx'}
  ];

}]);
