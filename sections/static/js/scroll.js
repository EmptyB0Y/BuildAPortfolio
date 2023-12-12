function scrollMedia(direction) {
  const mediaList = document.getElementById('skills-scroller');
  const scrollAmount = 200; // Adjust as needed

  if (direction === 'left') {
      mediaList.scrollLeft -= scrollAmount;
  } else if (direction === 'right') {
      mediaList.scrollLeft += scrollAmount;
  }

    // Check if the scroll position is at the end and adjust for looping
    if (direction === 'left' && mediaList.scrollLeft <= 0) {
      mediaList.scrollLeft = mediaList.scrollWidth;
  } else if (direction === 'right' && mediaList.scrollLeft + mediaList.clientWidth >= mediaList.scrollWidth) {
      mediaList.scrollLeft = 0;
  }
}

let leftPaddle = document.getElementById('left-paddle');
let rightPaddle = document.getElementById('right-paddle');

leftPaddle.addEventListener("click",function(e){
  scrollMedia('left')
})

rightPaddle.addEventListener("click",function(e){
  scrollMedia('right')
})
