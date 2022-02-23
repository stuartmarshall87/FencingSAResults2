$(window).on('load', function () {
    var date = getParameterByName('date', window.location.search.toLowerCase());
    var category = getParameterByName('category', window.location.search.toLowerCase());
    var weapon = getParameterByName('weapon', window.location.search.toLowerCase());
    var gender = getParameterByName('gender', window.location.search.toLowerCase());
    gender = gender == null ? '' : gender;
    var name = getParameterByName('name', window.location.search.toLowerCase());
    name = name == null ? '' : name;
    var year = date.substring(0, 4);
    var month = date.substring(4, 6);
    var day = date.substring(6, 8);
    var dateName = getDateString(day, month, year);

    // Platform E=Engarde, L=Legacy, F=Fencing Time, B=Bellepoule
    var platform = getParameterByName('platform', window.location.search.toLowerCase());
    
    var categoryString = getCategoryString(category);
    var weaponString = getWeaponName(weapon);
    var genderString = getGenderName(gender);
    var nameString = getCompName(name, gender);
    var comp = dateName + ' ' + nameString + ' ' + categoryString + ' ' + genderString + ' ' + weaponString;
    $("#compTitle").text(comp);
    var compCode = date + category + gender + weapon;     


    const repoPath = "./";
    if(platform == 'E') {
        $('head').append('<link rel="stylesheet" href="' + repoPath + 'style.css" type="text/css"/>');
        $('head').append('<link rel="stylesheet" href="' + repoPath + 'print.css" type="text/css"/>');
        $('#tabs').show();
        var path = repoPath + year + "/" + compCode.toUpperCase();
        $.get(path + 'F' + ".htm" + "?timestamp=" + (new Date()).getTime(), function(data) {
            $('#fencers').html(data);
        });
        $.get(path + 'P' + ".htm" + "?timestamp=" + (new Date()).getTime(), function(data) {
            $('#poules').html(data);
        });
        $.get(path + 'T' + ".htm" + "?timestamp=" + (new Date()).getTime(), function(data) {
            $('#tableau').html(data);
        });
        $.get(path + 'R' + ".htm" + "?timestamp=" + (new Date()).getTime(), function(data) {
            $('#ranking').html(data);
        });
        $('#tabNav').tabs()
    }
    else {
        var path = repoPath + year + "/" + compCode.toUpperCase() + ".html" + "?timestamp=" + (new Date()).getTime();
        $.get(path, function (data) {
            $('.tabs').html(data);
        });
    }
});

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    regex = new RegExp("[?" + String.fromCharCode(38) + "]" + name + "=[^" + String.fromCharCode(38) + "]*");
    var result = regex.exec(url);
    var parts = result == null ? '' : result[0].split('=');
    if (!parts) return null;
    if (!parts[1]) return '';
    return decodeURIComponent(parts[1].replace(/\+/g, " "));
};

function getCategoryString(category){
    var categoryString = category;
    switch (category.toLowerCase()) {
        case "oa": categoryString = 'Open A';
            break;
        case "ob": categoryString = 'Open B';
            break;
        case "ca": categoryString = 'Cadet A';
            break;
        case "cb": categoryString = 'Cadet B';
            break;
        case "o": categoryString = 'Open';
            break;
        case "i": categoryString = 'Intermediate';
            break;
        case "n": categoryString = 'Novice';
            break;
        case "ot": categoryString = 'Open Teams';
            break;
        case "u9": categoryString = 'U9';
            break;
        case "u11": categoryString = 'U11';
            break;
        case "u13": categoryString = 'U13';
            break;
        case "u13t": categoryString = 'U13 Teams';
            break;
        case "u14t": categoryString = 'U14 Teams';
            break;
        case "t": categoryString = 'Teams';
            break;
        case "u15": categoryString = 'U15';
            break;
        case "u1720": categoryString = 'U17/U20';
            break;
        case "v": categoryString = 'Veterans';
            break;
        case "yi": categoryString = 'Youth Intermediate';
            break;
        case "vt": categoryString = 'Veteran Teams';
            break;
    } 
    return categoryString;
}

function getDateString(day, month, year){    
    var monthName;
    
    switch (month) {
        case "01":
            monthName = ' January ';
            break;
        case "02":
            monthName = ' Feburary ';
            break;
        case "03":
            monthName = ' March ';
            break;
        case "04":
            monthName = ' April ';
            break;
        case "05":
            monthName = ' May ';
            break;
        case "06":
            monthName = ' June ';
            break;
        case "07":
            monthName = ' July ';
            break;
        case "08":
            monthName = ' August ';
            break;
        case "09":
            monthName = ' September ';
            break;
        case "10":
            monthName = ' October ';
            break;
        case "11":
            monthName = ' November ';
            break;
        case "12":
            monthName = ' December ';
            break;
    }
    
    return day + ' ' + monthName + ' ' + year;
}

function getWeaponName(weapon){
    var weaponString = weapon;
    switch (weapon.toLowerCase()) {
        case "f": weaponString = 'Foil';
            break;
        case "e": weaponString = 'Epée';
            break;
        case "s": weaponString = 'Sabre';
            break;
    }
    return weaponString;
}

function getGenderName(gender){
    var genderString = '';
    var genderIndex = '';
    switch (gender.toLowerCase()) {
        case "w":
            genderString = 'Womens';
            genderIndex = 'Female';
            break;
        case "m":
            genderString = 'Mens';
            genderIndex = 'Male';
            break;
        case "b":
            genderString = 'Boys';
            genderIndex = 'Male';
            break;
        case "g":
            genderString = 'Girls';
            genderIndex = 'Female';
            break;
    }

    return genderString;
}

function getCompName(name, gender){
    var nameString = name == null ? '' : name;
    switch (nameString.toLowerCase()) {
        case "kbt":
            if (gender.toLowerCase() == "w") {
                nameString = 'Andrea Chaplin';
            } else {
                nameString = 'Kingsley B Thomsen';
            };
            break;
        case "bk":
            if (gender.toLowerCase() == "w") {
                nameString = 'Coraine Sopru';
            } else {
                nameString = 'Bruce Kneale';
            };
            break;
        case "sc":
            nameString = 'State Championships';
            break;
        case "fcc":
            nameString = 'Future Championship Cup';
            break;
        case "mc":
            nameString = 'Meredith Coleman';
            break;
        case "amg":
            nameString = 'Australian Masters Games';
            break;
        case 'saschools':
            nameString = 'SA Schools Championships';
            break;
    }
    return nameString;
}