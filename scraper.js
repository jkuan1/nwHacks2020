const axios = require('axios');
const cheerio = require('cheerio');

//recieve tab from backend

function webScrapper (tab){
    axios(tab)
    .then((response) => {
        const $ = cheerio.load(response.data);
        const firstUrl = $('body').find('img').attr('src')
        console.log(firstUrl)
    }).catch(() => console.log('something went wrong!'))
}

  