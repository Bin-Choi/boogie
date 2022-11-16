<template>
  <li>
    <!-- <div class="popupVideo">
      <a href="#layer" @click="openlayer"><iframe :src="videoURL" frameborder="0" width="300" height="200" allowfullscreen></iframe>
      {{video.snippet.title}}
      </a>
    </div>
    <div id="layer">
      <div class="inner">
        <div class="cont">
          <iframe id="player" width="560" height="315" :src="videoURL" frameborder="0" allowfullscreen></iframe>
        </div>
        <a herf="#none" class="close">close</a>
      </div>
    </div>
    <div class ="dim"></div> -->
    <!-- <div class="page">
      <a href="#layer" class="button"><iframe id="player" width="560" height="315" src="https://www.youtube.com/embed/CUFwL9KYfIU" frameborder="0" allowfullscreen></iframe>{{movie.title}}</a>
    </div>

    <div id="layer">
      <div class="inner">
        <div class="cont">
          <iframe id="player" width="560" height="315" src="https://www.youtube.com/embed/CUFwL9KYfIU" frameborder="0" allowfullscreen></iframe>
        </div>
        <a href="#none" class="close">close</a>
      </div>
    </div>
    <div class="dim"></div> -->
    <iframe id="player" width="300" height="200" :src="videoURL" frameborder="0" allowfullscreen></iframe>
    <p>{{video.snippet.title}}</p>

  </li>

</template>

<script>
// import $ from 'jequery';

export default {
  name: "VideoListItem",
  props: {
    video: Object,
  },

  methods: {
    play(){
      this.$emit('play', this.video)
    },
    // openlayer(){

    //   let path = this.attr('href')
    //   this.cont.append(this.embed)
    //   path.show()
    //   this.dim.show()
    // }

  },
  computed: {
    videoURL(){
      return "https://www.youtube.com/embed/" + this.video.id.videoId 
    },

  },
}


// $(function(){
  
// 	var embed = $('#player'); //동영상 코드
  
// 	$('.button').on('click', function(){ //레이어 열때
// 		var path = $(this).attr('href');
// 		$('.cont').append(embed);
// 		$(path).show();
// 		$('.dim').show();
// 	})
  
// 	$('.close').on('click', function(){ //레이어 닫을때
// 		$(this).parents('#layer').hide();
// 		$('.dim').hide();
// 		$('.cont').empty();
// 	})
  
//   $('.dim').on('click', function(){
//     $(this).hide();
//     $('#layer').hide();
//     $('.cont').empty();
//   })
  
// });
// </script>

<style>
  li {
    display: flex;
  }
</style>
