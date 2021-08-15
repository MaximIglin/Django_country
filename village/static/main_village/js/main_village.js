//Add consts, which contains urls to DRF
const VILLAGES_API_URL = "http://127.0.0.1:8000/api/villages/";
const VILLAGE_PHOTOS_API_URL = "http://127.0.0.1:8000/api/village_images/";
const VILLAGE_NEWS_API = "http://127.0.0.1:8000/api/village_news/"

//Open and Send XHR object
const VILLAGES_API = new XMLHttpRequest();
VILLAGES_API.open("GET", VILLAGES_API_URL);
VILLAGES_API.responseType = 'json';
let container = document.getElementById("container")

//Do all, when DOMContentLoaded
document.addEventListener("DOMContentLoaded", function () {
    const VILLAGE_NAME = document.getElementById("village_name").innerHTML;
    let correct_village; //declare a variables in which we write the correct village below and that id
    let correct_village_id; 
    VILLAGES_API.onload = () => {
        let all_data = VILLAGES_API.response;
        for (let i in all_data) {
            if (all_data[i].title == VILLAGE_NAME) {
                correct_village = all_data[i];// add correct village and that id,iterating over the json array
                correct_village_id = all_data[i].id;
                break;
            }
        }
    }
    setTimeout(function () {
        //add eventListners to all btns and add information in container
        document.getElementById("btn1").addEventListener("click", function () {
            container.innerHTML = "<h2>О населённом пункте</h2>"
            //window.history.replaceState(null,"page1",'about');
            container.innerHTML += correct_village.all_information;
        })
        document.getElementById("btn2").addEventListener("click", function () {
            //window.history.replaceState(null,"page1",'history');
            container.innerHTML = "<h2>Историческая справка</h2>"
            container.innerHTML += correct_village.historical_informaion;
        })
        document.getElementById("btn3").addEventListener("click",function(){
            //window.history.replaceState(null,"page1",'at_the_moment');
            container.innerHTML = "<h2>Ситуация на данный момент</h2>"
            container.innerHTML += correct_village.at_the_moment
        })
        document.getElementById("btn4").addEventListener("click",function(){
            //window.history.replaceState(null,"page1",'photos');
            const PHOTOS_API = new XMLHttpRequest;
            PHOTOS_API.open("GET",VILLAGE_PHOTOS_API_URL);
            PHOTOS_API.responseType = 'json';
            let correct_photos = [];
            PHOTOS_API.onload = () =>{
                let all_photos = PHOTOS_API.response;
                for (let i in all_photos){
                    if (all_photos[i].village_name == correct_village_id){
                        correct_photos.push(all_photos[i]);
                        
                    }
                }
            }
            
            setTimeout(function(){
                container.innerHTML = '<div class="add_photos"><h2>Фотографии</h2> </div> <div id="images_wrap"></div>' ;
                for (i in correct_photos){
                    document.getElementById("images_wrap").innerHTML += `<img src=${correct_photos[i].image} style="width:320px; height:230px;" class="img-fluid">`
                }
            },100)

            PHOTOS_API.send();
        })
        document.getElementById("btn5").addEventListener("click",function(){
            //window.history.replaceState(null,"page1",'News');
            const API_NEWS = new XMLHttpRequest;
            API_NEWS.open("GET", VILLAGE_NEWS_API);
            API_NEWS.responseType = 'json';
            let correct_news = [];
            API_NEWS.onload = () =>{
                let all_news = API_NEWS.response;
                for (let i in all_news){
                    if(all_news[i].village_name == correct_village_id)
                    correct_news.push(all_news[i])
                }
            }
            setTimeout(function(){
                container.innerHTML = '<h2 class="news_page_title">Новости</h2>';
                for(i in correct_news){
                    container.innerHTML += `<div class="news_container" id="news"><img src="${correct_news[i].images.image[0]}" class="news_image"><div class="news_information"><div class="title_and_date"><h3 class="news_title">${correct_news[i].title}</h3><span class="news_date">${correct_news[i].date}</span></div><p class="article">${correct_news[i].short_text_of_news}</p></div></div></div>`;
                }
                for (let n in correct_news){
                    document.getElementsByClassName("news_container")[n].addEventListener("click",function(){
                        container.innerHTML = "";
                        container.innerHTML = `<h2>${correct_news[n].title}</h2>`
                        container.innerHTML += '<div id="news_images"></div>'
                        for (let k in correct_news[n].images.image)
                            document.getElementById("news_images").innerHTML += `<img src="${correct_news[n].images.image[k]} class="news_image_all" style="margin-right:15px; ">`
                        container.innerHTML += `<p style="font-size:35px;">${correct_news[n].text_of_news}<p><br>`
                        
                        
                    })
                }

            },500)
            
            API_NEWS.send()
        })
        document.getElementById("btn6").addEventListener("click",function(){
            //window.history.replaceState(null,"page1",'possibilities');
            container.innerHTML = "<h2>Возможности для предпринимателей</h2>"
            container.innerHTML += correct_village.possibilities
        })
    }, 700)

    VILLAGES_API.onerror = () => {
        alert("Произошла ошибка")
    }
    VILLAGES_API.send();
});
