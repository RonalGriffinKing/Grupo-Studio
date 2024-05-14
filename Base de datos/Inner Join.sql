select * from fabricantes F inner join producto p on f.codigo=p.codigo_fabricante 
where nombre=asus;

select count (p.codigo)from fabricantes F inner join producto p on f.codigo=p.codigo_fabricante 
where nombre=asus;


select f.nombre, count(p.codigo) from fabricante F inner join producto p on f.codigo=p.codigo_fabricante group by f.codigo having count(p.codigo) >=( select  from fabricante F inner join producto p on F.codigo=0)