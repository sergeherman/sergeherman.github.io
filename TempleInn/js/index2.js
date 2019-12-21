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
                let address = document.createElement('h3');
                let telephone = document.createElement('p');
                let services = document.createElement('p');
                let history = document.createElement('p');
				let ordinanceSession = document.createElement('p');
				let templeClosure = document.createElement('p');
				


                name.textContent = towns[i].name;
                address.textContent = towns[i].address;
                telephone.textContent = 'Telephone: ' + towns[i].telephoneFounded;
                services.textContent = 'Services: ' + towns[i].currentservices;
                history.textContent = 'Annual Rain Fall: ' + towns[i].averageRainfall + ' in';
				services.textContent = 'Ordinance and Session Schedule: ' + towns[i].ordinanceSession;
				services.textContent = 'Temple Closure Shedule: ' + towns[i].templeClosure;
			
                

                card.appendChild(name);
                card.appendChild(address);
                card.appendChild(telephone);
                card.appendChild(services);
                card.appendChild(history);
                card.appendChild(ordinanceSession);
				card.appendChild(templeClosure);
				

                document.querySelector('div.cards').appendChild(card);
            }
        }
    });