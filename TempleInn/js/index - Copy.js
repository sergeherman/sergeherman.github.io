const requestURL = 'https://byui-cit230.github.io/weather/data/towndata.json';

fetch(requestURL)
    .then(function(response) {
        return response.json();
    })
    .then(function(jsonObject) {

        const towns = jsonObject['towns'];

        for (let i = 0; i < towns.length; i++) {
            if (towns[i].name == 'Fish Haven' || towns[i].name == 'Preston' || towns[i].name == 'Soda Springs') {
                let card = document.createElement('section');
                let name = document.createElement('h2');
                let motto = document.createElement('h3');
                let year = document.createElement('p');
                let population = document.createElement('p');
                let aveRainfall = document.createElement('p');
                let image = document.createElement('img');

                name.textContent = towns[i].name;
                motto.textContent = towns[i].motto;
                year.textContent = 'Year founded: ' + towns[i].yearFounded;
                population.textContent = 'Current Population: ' + towns[i].currentPopulation;
                aveRainfall.textContent = 'Annual Rain Fall: ' + towns[i].averageRainfall + ' in';
                image.setAttribute('src', 'images/' + towns[i].photo);

                card.appendChild(name);
                card.appendChild(motto);
                card.appendChild(year);
                card.appendChild(population);
                card.appendChild(aveRainfall);
                card.appendChild(image);

                document.querySelector('div.cards').appendChild(card);
            }
        }
    });