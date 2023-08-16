//start of reading file

fetch('people.json')
.then(response => response.json())


.then(data => {
    //counter for numbering people
    let counter = 1
    data.forEach(people => {
        console.log(`Person: ${counter}`)
        //out putting peoples info in formatted way to console
        console.log(`This person named ${people.firstname} ${people.lastname} lives in ${people.city} and gender is ${people.gender}`)
        counter ++

        
    });


//catch any errors
})
.catch(error => {
    console.error(error);
})