-- Use 'hbtn_0d_tvshows' to list all genres not linked to show 'Dexter'
-- 'tv_shows' table contains only one record where title = Dexter
-- Each record should display tv_genres.name
-- Results must be sorted ascending order by genre name
-- You can use max of two SELECT statements
SELECT gtv.name FROM tv_genres g WHERE gtv.name NOT IN (
      SELECT gtv.name
      FROM tv_genres gtv
      INNER JOIN tv_show_genres mo ON gtv.id = mo.genre_id
      INNER JOIN tv_shows so ON mo.show_id = so.id
      WHERE so.title = 'Dexter'
) ORDER BY gtv.name ASC;