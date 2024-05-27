% tech_recommendations.pl
% Base de dados de tecnologias
tech('HTML', front_end).
tech('CSS', front_end).
tech('JavaScript', front_end).
tech('React', front_end).
tech('Angular', front_end).
tech('Vue.js', front_end).
tech('Python', back_end).
tech('Django', back_end).
tech('Flask', back_end).
tech('Java', back_end).
tech('Spring', back_end).
tech('Node.js', back_end).
tech('Ruby on Rails', back_end).
tech('JavaScript', fullstack).
tech('Node.js', fullstack).
tech('React', fullstack).
tech('Vue.js', fullstack).
tech('Angular', fullstack).
tech('Python', fullstack).
tech('Django', fullstack).
tech('Java', fullstack).
tech('Spring', fullstack).

% Recomendação baseada na área de desenvolvimento
recommend_tech(Role, Tech) :-
    tech(Tech, Role).
