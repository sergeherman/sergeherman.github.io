const requestURL = 'https://sergeherman.github.io/TempleInn/Data/towndata.json';

fetch(requestURL)
    .then(function(response) {
        return response.json();
    })
    .then(function(jsonObject) {

        const towns = jsonObject['towns'];

        for (let i = 0; i < towns.length; i++) {
           if (towns[i].name == 'Rome Italy Temple' || towns[i].name == 'Paris France Temple' || towns[i].name == 'Copenhagen Denmark Temple' || towns[i].name == 'The Hague Netherlands Temple') {
                let card = document.createElement('section');
                let name = document.createElement('h2');
                let motto = document.createElement('h3');
                let year = document.createElement('p');
				let population = document.createElement('p');
                let aveRainfall = document.createElement('p');
				let events = document.createElement('p');
               

                name.textContent = towns[i].name;
                motto.textContent = towns[i].motto;
                year.textContent = 'Temple History: ' + towns[i].yearFounded;
				population.textContent = 'Services: ' + towns[i].currentPopulation;
                aveRainfall.textContent = 'Session Schedule: ' + towns[i].averageRainfall;
				events.textContent = 'Temple closures: ' + towns[i].events;
				
          

                card.appendChild(name);
                card.appendChild(motto);
                card.appendChild(year);
                card.appendChild(population);
                card.appendChild(aveRainfall);
				card.appendChild(events);
                

                document.querySelector('div.cards').appendChild(card);
            }
        }
    });