function deleteOpinion(opinion_id, opinion_user_id, movie_id) {
    fetch("/delete-opinion", {
    // fetch("/opionons/$(opinion_id)", {
        method: "POST",
        body: JSON.stringify({
            opinion_id: opinion_id,
            opinion_user_id: opinion_user_id
        })
    }).then((_res) => {
        window.location.href = `/movies/${movie_id}`;
    });
}