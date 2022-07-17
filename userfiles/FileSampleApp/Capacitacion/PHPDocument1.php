<?php
$states = array(
				array('Buenos Aires','Córdoba','Rosario','Mendoza','Santa Fe'),
				array('Madrid','Valencia','Barcelona','Pamplona'),
				array('Distrito Federal','Monterrey','Guadalajara'),
				array('La Victoria','Piura','Surco','Lima'),
				array('Texas','California','New york','Virginia')
			   );
			   
			   
function toJSON($array)
{
	$data=array(); $i=0;
	$total = count($array);
	foreach($array as $key=>$value)
	{
		array_push($data,array
		(
			'value'=>$i++,
			'label'=>$value
		));
	}
	
	return json_encode(array(
		'total'=>$total,
		'data'=>$data
	));
}

echo toJSON($states[2]);
?>