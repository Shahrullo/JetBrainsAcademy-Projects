let keys = ['KeyA', 'KeyS', 'KeyD', 'KeyF', 'KeyG', 'KeyH', 'KeyJ', 'KeyW',
            'KeyE', 'KeyT', 'KeyY', 'KeyU'];

document.addEventListener("keypress", function (event) {
   if (keys.includes(event.code)) {
       console.log(`The '${event.key}' key is pressed`);
       let audio = document.createElement('AUDIO');
       audio.src = `white_keys/${event.key}.mp3`;
       audio.play();
   } else {
       console.log("Warning! Pressed incorrect key!!!")
       alert('Wrong Keyword')
   }
});

