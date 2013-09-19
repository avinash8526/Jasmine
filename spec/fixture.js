describe("Testing fixtures",function(){

	it("expects that loadFixtures is defined",function(){

		expect(loadFixtures).toBeDefined();
	});

	it("loads specrunner.html",function(){
		loadFixtures("SpecRunne.html");
	});
	
});