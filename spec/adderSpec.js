describe("To verify that adder method is working fine", function(){

	// beforeEach(function(){
	// 	a = 12;

	// });

	it("it will add two numbers",function(){
		expect(Adder.add(2,3)).toEqual(5);

	});

	xit("shoul expect a to be true",function(){
		//var a = 12;
		expect(a).toBeDefined();
	})	

});

describe("A spy implementation",function(){

	beforeEach(function(){
		spyOn(Adder, 'add');

		Adder.add(2, 3);


	});
	

	it("tracks that the spy was called", function() {
    expect(Adder.add).toHaveBeenCalled();
  });

	it("tracks the value which was passed to spy",function(){
		expect(Adder.add).toHaveBeenCalledWith(2,3);
	});

});

describe("jasmine.any", function() {

  it("matches any value", function() {
    expect({}).toEqual(jasmine.any(Object));
    expect(12).toEqual(jasmine.any(Number));
  });
 }); 