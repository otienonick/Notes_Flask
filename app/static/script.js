function deleteNote(noteId){
    // send a request using fetch
    fetch('/delete-note',{
        method: 'POST',
        body: JSON.stringify({noteId:noteId})
        
    }).then((_res) => {
        window.location.href = '/'
    });
}