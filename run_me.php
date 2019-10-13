#!/usr/bin/php
<?php

#the general idea flow of this is
#		make the query url for the data that you want to grab
#		json_decode() the responce to get a php variable
#		then loop through each array in the array until you get the id you want
#		then make a variable of that and return it

# todo
# function to grab routes along path ,
# let user pick which station to start // end at when multiple return results
# do the fun part of the project ie (the routeing algorythm)
class navitia_query
{
	private		$base_url = 'https://api.navitia.io/v1/coverage/fr-idf/';
	# fill me in
	private		$auth_token = '66d766fa-4408-4dfd-be38-21e851a208cb';
	# is this the right syntax ?

	#goes through the array of arrays
	private function nearest_s(array $data)
	{
		$cords = array();
		$tmp = $data['places'];
		$i = 0;
		while ($i < sizeof($tmp))
		{
			$flag = 0;
			if ($tmp[$i]['embedded_type'] === 'stop_area')
			{
				$tmp1 = $tmp[$i]['stop_area']['commercial_modes'];
				if (isset($tmp1))
				{
					$j = 0;
					$tmp2 = $tmp[$i]['stop_area']['commercial_modes'];
					while ($j < sizeof($tmp2))
					{
						if ($tmp2[$j]['name'] == 'Métro')
							$flag = 1;
						$j++;
					}
				}
				if ($flag == 1)
				{
					$cords[] = array('label' => $tmp[$i]['stop_area']['label'],
						'id' => $tmp[$i]['stop_area']['id']);
				}
			}
			$i++;
		}
		return ($cords);
	}

	private function make_api_query(string $url)
	{
		$qu = $this->calc_query_url($url);
		$cu = curl_init();
		curl_setopt($cu, CURLOPT_URL, $qu);
		curl_setopt($cu, CURLOPT_USERPWD, $this->auth_token);
		#curl return string instead
		curl_setopt($cu, CURLOPT_RETURNTRANSFER, true);
		$out = curl_exec($cu);
#for testing we can cache the file
	#	$out = file_get_contents('test.json');
		curl_close($cu);
		#return an array instead of the object
		return json_decode($out, true);
	}

	# hey look it's strjoin
	# adds the query component to the base url
	private function calc_query_url($url)
	{
		return $this->base_url . $url;
	}

	#get metro station
	public function get_metro($place1)
	{
		$query = 'places?q=' . $place1 . '&type[stoppoint]=address';
		$return_v = $this->make_api_query($query);
		#return a nearby metro station
		return $this->nearest_s($return_v);
	}

}

$len = count($argv);
if ($len == 3)
{
	if (strlen($argv[1]) > 0 && strlen($argv[2]) > 0)
	{
		$cl = new navitia_query();
		$station_start = $cl->get_metro(preg_replace("/[\s]+/", '%', trim($argv[1])));
		$station_final = $cl->get_metro(preg_replace("/[\s]+/", '%', trim($argv[2])));
		echo "station start == ";
		print_r($station_start);
		echo "\n";
		echo "station final == ";
		print_r($station_final);

		#not sure if you guys wanna do php or not , this puts it back into json
		file_put_contents('tmp_start.json', json_encode($station_start));
		file_put_contents('tmp_final.json', json_encode($station_final));
		#test
		#print_r($cl->make_api_query(''));
		#print_r($cl->get_metro($argv[1]));
	}
	else
		echo "please input two valid strings";
}
else
	echo "usage :: php run_me start_dest end_dest";
?>
